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


def retransmit(message_no, channel_no):
    """
    メッセージを再送信するためのリクエストを送信します。

    引数:
        message_no (int): メッセージ番号
        channel_no (int): チャンネル番号

    返値:
        dict: レスポンスのJSONデータ
    """
    url = f"https://talk.worksmobile.com/p/oneapp/client/chat/retransmit?messageNo={message_no}&channelNo={channel_no}"

    try:
        response = requests.get(url, headers=nheaders)
        response.raise_for_status()  # HTTP エラーの場合に例外を発生させる
        return response.json()  # JSON形式でレスポンスを返す
    except requests.exceptions.RequestException as e:
        print(f"Error retransmitting message {message_no} in channel {channel_no}: {e}")
        return None


# サンプル使用
message_no = 300
channel_no = 291365148
response_data = retransmit(message_no, channel_no)
print(response_data)
