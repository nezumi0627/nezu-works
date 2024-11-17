import json
import time

import requests

LOGIN_PAGE_URL = "https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/"
ORIGIN = "https://talk.worksmobile.com"
LOGIN_URL = "https://auth.worksmobile.com/login/loginProcessV2"

input_id = "nium.nezumi@nezumi-developer"
password = "n@20080627"  # パスワードは環境変数で管理することを推奨
domainId = 400492334
userNo = 110002509311906
channelNo = 290030852
tempMessageId = 64663310


def login(input_id, password):
    """
    Worksmobileサービスにログインし、セッションクッキーをJSON文字列として返します。

    Args:
        input_id (str): ユーザーのアカウントID。
        password (str): パスワード。

    Returns:
        str: ログインが成功した場合はセッションクッキーをJSON文字列で返します。
             ログインに失敗した場合はNoneを返します。
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": f"{LOGIN_PAGE_URL}&loginParam={input_id}",
        "Origin": ORIGIN,
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
    }

    try:
        login_page_response = requests.get(LOGIN_PAGE_URL, headers=headers)
        login_page_response.raise_for_status()

        payload = {
            "accessUrl": "https://talk.worksmobile.com/",
            "inputId": input_id,
            "password": password,
            "keepLoginYn": "N",
        }

        response = requests.post(LOGIN_URL, headers=headers, data=payload, allow_redirects=False)
        response.raise_for_status()

        cookies_dict = {cookie.name: cookie.value for cookie in response.cookies}
        cookies_json = json.dumps(cookies_dict, indent=4, ensure_ascii=False)

        return cookies_json

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None


def cookies_to_header(cookies_dict):
    """
    クッキー辞書をCookieヘッダー文字列に変換します。

    Args:
        cookies_dict (dict): クッキーの辞書。

    Returns:
        str: Cookieヘッダーの値。
    """
    return "; ".join(f"{name}={value}" for name, value in cookies_dict.items())


cookies_json = login(input_id, password)

if cookies_json:
    cookies_dict = json.loads(cookies_json)
    nheaders = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Cookie": cookies_to_header(cookies_dict),
    }

    payload = {
        "serviceId": "works",
        "channelNo": channelNo,
        "tempMessageId": tempMessageId,
        "caller": {"domainId": domainId, "userNo": userNo},
        "extras": {
            "activeUserCount": 1,
            "activeUserList": [{"domainId": 0, "id": 913000007588432, "name": "The Test Log."}],
            "botInfo": None,
            "excludeExtraUserCount": 0,
            "excludeUserCount": 0,
            "excludeUserList": [],
            "extraUserCount": 0,
            "extraWaitBuddyCount": 0,
            "flags": [],
            "historyMode": 0,
            "inactiveExtraUserCount": 0,
            "inactiveUserCount": 0,
            "inactiveUserList": [],
            "inviter": {"domainId": 0, "i18nNames": [], "id": 0, "name": ""},
            "requestService": "",
            "title": "N-TEST",
            "waitBuddyList": [],
        },
        "type": 101,
    }

    payload["extras"] = json.dumps(payload["extras"])

    def send_request():
        response = requests.post(
            "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage", headers=nheaders, json=payload
        )
        if response.status_code == 429:
            print("Too Many Requests. Stopping...")
            raise Exception("Too Many Requests")
        return response.json()

    def main():
        try:
            response = send_request()
            print(response)
        except Exception as e:
            print(f"Error: {e}")

    if __name__ == "__main__":
        start_time = time.time()
        main()
        print("Elapsed Time:", time.time() - start_time)
