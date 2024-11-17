import json
import time

import requests

LOGIN_PAGE_URL = "https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/"
Origin = "https://talk.worksmobile.com"
LOGIN_URL = "https://auth.worksmobile.com/login/loginProcessV2"

input_id = "yamaoka.usmiyu@sugiwaranonono"
password = "n@20080627"


def login(input_id, password):
    """
    Worksmobileサービスにログインし、セッションクッキーをJSON文字列として返します。

    Args:
        input_id (str): ユーザーのアカウントID
        password (str): パスワード

    Returns:
        str: ログイン成功時のセッションクッキーのJSON文字列、ログイン失敗時はNone
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

    Args:
        cookies_dict (dict): クッキーの辞書

    Returns:
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


def search_and_fetch_messages(keyword, start=0, display=1000, channel_no=291108891, msg_types=None):
    """
    指定したチャンネルからキーワードに基づいてメッセージを検索・取得する関数。

    Args:
        keyword (str): 検索キーワード
        start (int): 取得開始位置（デフォルトは0）
        display (int): 取得するアイテム数（デフォルトは1000）
        channel_no (int): チャンネル番号（デフォルトは291108891）
        msg_types (str): メッセージタイプのリスト（デフォルトはNone）

    Returns:
        dict: レスポンスデータの辞書
    """
    if msg_types is None:
        msg_types = "1:3:4:5:6:7:8:10:11:12:13:14:16:17:19:22:23:24:25:26:27:28:29:30:37:39:44:46:47:48:49:96:97:98"
    timestamp = str(int(time.time() * 1000))  # 現在のタイムスタンプをミリ秒で取得

    payload = {
        "keyword": keyword,
        "start": start,
        "display": display,
        "channelNo": channel_no,
        "msgType": msg_types,
        "timeStamp": timestamp,
    }

    url = "https://talk.worksmobile.com/p/oneapp/client/search/searchChannel"

    print(f"リクエストURL: {url}")  # デバッグ用のログ出力
    print(f"リクエストボディ: {payload}")  # デバッグ用のログ出力

    response = requests.post(url, headers=nheaders, json=payload)  # POSTメソッドでリクエストボディを送信

    print(f"レスポンスステータスコード: {response.status_code}")  # デバッグ用のログ出力
    print(f"レスポンス内容: {response.text}")  # デバッグ用のログ出力

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


print(search_and_fetch_messages("あ"))
