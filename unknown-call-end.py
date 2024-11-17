import json

import requests

input_id = "yamaoka.usmiyu@sugiwaranonono"
password = "n@20080627"

LOGIN_URL = "https://auth.worksmobile.com/login/loginProcessV2"
LOGIN_PAGE_URL = "https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/"
Origin = "https://talk.worksmobile.com"


def login(input_id, password):
    """
    Worksmobileサービスにログインし、セッションクッキーをJSON文字列として返します。

    引数:
        input_id (str): ユーザーのアカウントID
        password (str): パスワード

    返値:
        str: ログイン成功時のセッションクッキーのJSON文字列。失敗時はNone。
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


# ログインしてクッキーを取得
cookies_json = login(input_id, password)

# ヘッダーの設定
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


def group_change():
    """
    指定されたJSONデータをPOSTリクエストとして送信します。
    """

    url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"  # 実際のURLに合わせて変更してください

    payload = {
        "serviceId": "works",
        "channelNo": 291365148,
        "tempMessageId": 485225460,
        "caller": {"domainId": 400495509, "userNo": 110002509337378},
        "extras": "",
        "titel": "sw",
        "content": "fqw",
        "type": 110,
    }

    try:
        response = requests.post(url, headers=nheaders, json=payload)
        response.raise_for_status()  # HTTP エラーの場合に例外を発生させる
        print("データが正常に送信されました。")
        print(response.json())  # レスポンスが JSON 形式の場合は表示
    except requests.exceptions.RequestException as e:
        print(f"データの送信中にエラーが発生しました: {e}")


# 関数の実行
group_change()