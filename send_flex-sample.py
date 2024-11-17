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


def send_message(message_type):
    """
    指定されたタイプのメッセージを送信します。

    引数:
        message_type (int): メッセージのタイプ

    返値:
        None
    """

    payload = {
        "serviceId": "works",
        "channelNo": 291365148,
        "tempMessageId": 485225460,
        "caller": {"domainId": 400495509, "userNo": 110002509337378},
        "extras": {
            "ALT_TEXT": "このメッセージには画像が含まれています。",
            "FLEX_JSON": json.dumps(
                {
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "url": "https://alice.worksmobile.com/clover/line_v3/yamaoka.usmiyu@sugiwaranonono",
                        "aspectRatio": "1.51:1",
                        "aspectMode": "cover",
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "paddingAll": "13px",
                        "paddingBottom": "17px",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ねずわーくす - 無料多機能BOT",
                                "size": "16px",
                                "color": "#000000",
                                "weight": "bold",
                                "lineSpacing": "5px",
                                "offsetTop": "-3px",
                                "wrap": True,
                            },
                            {
                                "type": "text",
                                "text": "Nezumi-Project2024",
                                "size": "14px",
                                "color": "#555555",
                                "margin": "4px",
                                "lineSpacing": "3px",
                                "wrap": True,
                            },
                        ],
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "paddingAll": "0px",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "paddingTop": "14px",
                                "paddingBottom": "13px",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "height": "30px",
                                        "justifyContent": "center",
                                        "action": {
                                            "type": "uri",
                                            "label": "友だち追加",
                                            "uri": "https://works.do/R/ti/p/yamaoka.usmiyu@sugiwaranonono",
                                        },
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "友だち追加",
                                                "size": "15px",
                                                "color": "#42659a",
                                                "align": "center",
                                                "wrap": False,
                                            }
                                        ],
                                    }
                                ],
                            }
                        ],
                    },
                    "styles": {"footer": {"separator": True, "separatorColor": "#e5e5e5"}},
                }
            ),
        },
        "type": message_type,
    }

    payload["extras"] = json.dumps(payload["extras"])

    try:
        response = requests.post(
            "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage", headers=nheaders, json=payload
        )
        response.raise_for_status()  # HTTP エラーの場合に例外を発生させる
        print(f"Message with type {message_type} sent successfully.")
        print(response.json())  # レスポンスが JSON 形式の場合は表示
    except requests.exceptions.RequestException as e:
        print(f"Error sending message with type {message_type}: {e}")


# メインスクリプト
if cookies_json:
    for message_type in range(1, 201):  # 1 から 200 までのメッセージタイプで送信
        send_message(message_type)
