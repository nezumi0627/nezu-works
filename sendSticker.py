import json
import time

import requests

LOGIN_PAGE_URL = "https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/"
Origin = "https://talk.worksmobile.com"
LOGIN_URL = "https://auth.worksmobile.com/login/loginProcessV2"

input_id = "yamaoka.usmiyu@sugiwaranonono"
password = "n@20080627"
domainId = 400492334
userNo = 110002509311906
channelNo = 291108765
tempMessageId = 64663310
# with open("death.txt", "r", encoding="utf-8") as f:
#     pkgVer = f.read()
#     stkOpt = f.read()
#     stkType = f.read()
# pkgId = f.read()
# stkId = f.read()
pkgVer = "3"
pkgId = "22795630"
stkId = "580968568"
stkType = "line"
stkOpt = "A"


def login(input_id, password):
    """
    Login to Worksmobile service and return session cookies as a JSON string.

    Args:
        input_id (str): The account ID of the user.
        password (str): The password.

    Returns:
        str: The session cookies as a JSON string if login is successful,
             None if login fails.
    """

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": f"{LOGIN_PAGE_URL}&loginParam={input_id}",
        "Origin": Origin,
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

    引数:
        cookies_dict (dict): クッキーの辞書

    返値:
        str: Cookieヘッダーの値
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
            "channelNo": channelNo,
            "pkgVer": pkgVer,
            "pkgId": pkgId,
            "stkId": stkId,
            "stkType": stkType,
            "stkOpt": stkOpt,
        },
        "type": 18,
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
        for _ in range(5):
            start_time = time.time()
            main()
            print("Elapsed Time:", time.time() - start_time)
