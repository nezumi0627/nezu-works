import json
import os
from urllib.parse import unquote

import requests

# ユーザー番号を指定し、その中のユーザーのみ反応させています
owners = [
    913000041624790,
    913000041325191,
    913000041775786,
    913000033734050,
    913000003889553,
    913000041941364,
    913000042405931,
]

domainId = 400460495
userNo = 110002509004447
tempMessageId = 434070220

# リクエストヘッダーとクッキー
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Cookie": "WORKS_LOGIN_TYPE=id;TZ=Asia/Tokyo;timezone=Asia/Tokyo;WORKS_TE_LOC=jp1;language=ja_JP;WORKS_RE_LOC=jp1;NEO_SES=AAABH63MrlaCKIK+hGSBvf2x2FHfdmpJuPwMNm6K2NEcZ87Lvn6PPnPozntYENcTQHA1TBWoybf0z3l4hPvAsbiwK8sDnayKIg+lgTAgjfR/vPsBCirtZolKFeopUNjlJgvOcxEge4s6R95LX697tD/XHqyIASgM2oH7YAxOMVcSopDDMJ1iM+KagDyWyoTJvE97Nvf/yj/vxu56u0jxRka9HIZBcSfWDJZnMVmTFBsWCIE7b77BPRDVup+JUu4RLE7zpRAQO35EwQAmuf5feBOQFlFc1FKkh5B7tDWqsS+A6zuWrHTSt1WgugC3AyzJBQ+Fa+TzYzwCyXKQKGIMQbWn0Jf+xr41PieYOQU74iBI/x8RVtXxUSvdHbKN88S36UQm8g==;WORKS_SES=eJwVjscRBEEIA1PCmycLQ/4hHfejSmrRNLFd8HiMUJriJSG5pTxc2K2pNBVHEb2iqUWKZFaJ5aSzlbthXNMJ177pja4LsOFten4fdD6u1/wNOH7ItYZ0q88Yrd40OKjERyo9k+ZzJfkeyFuuFKQZTwfKjupw4dSQIc3NENYp+2KgEKSPAnv44mT0f1jE1xanzsyxmVG8HFI2fqtjDON49FTbDgIcQ4T83iehQqH97ivn51nhQzJhwVW5katkTttzYZwjlQa0J2c5TDu3Kmvv7VQOZ8T04JyZFCDOD5tdVy0=;WORKS_USER_DOMAIN=mouse;WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw;LC=ja_JP;WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q",
}


# メッセージを受信して処理する関数
def receive_messages(headers):
    """
    Receive messages from the server and handle them.

    Args:
        headers (dict): The headers to be used in the HTTP request.

    """
    # Path to the file where received messages will be stored
    json_file_path = "received_messages.json"

    # Load previously received messages from the file
    received_messages = load_received_messages(json_file_path)

    # URL for the API endpoint
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/syncUserChannelList"

    # Payload for the API request
    payload = {
        "serviceId": "works",
        "userKey": {"domainId": domainId, "userNo": userNo},
        "filter": "none",
        "updatePaging": True,
        "pagingCount": 50,
        "userInfoCount": 8,
        "updateTime": 1717943403392,
        "beforeMsgTime": 0,
        "isPin": True,
        "requestAgain": False,
    }

    try:
        while True:
            # Send an HTTP POST request to the API endpoint
            response = requests.post(url, json=payload, headers=headers, timeout=30)

            # If the request was successful, handle the received messages
            if response.status_code == 200:
                handle_messages(response.json(), received_messages)
    except Exception as e:
        # If an exception occurred, print the error message
        print("エラー:", e)


def save_received_messages(received_messages, json_file_path):
    """
    Save the received messages to a file in JSON format.

    Args:
        received_messages (set): A set of received messages.
        json_file_path (str): The path to the JSON file.
    """
    # Open the JSON file in write mode
    with open(json_file_path, "w") as file:
        # Convert the received messages set to a list and dump it to the file
        json.dump(list(received_messages), file)


def load_received_messages(json_file_path):
    """
    Load received messages from a JSON file.

    Args:
        json_file_path (str): The path to the JSON file.

    Returns:
        set or list: A set or list of received messages.

    """
    # Check if the JSON file exists
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            # Load the data from the JSON file
            data = json.load(file)

            # Check if the data is a list
            if isinstance(data, list):
                # Convert the list data to a set if it contains lists
                # Otherwise, return the original data
                return {tuple(item) if isinstance(item, list) else item for item in data}
            else:
                # Print a warning if the data format is unexpected
                print("警告: JSONファイルのデータ形式が予期しないものです。")
                return set(data)  # Return the data as a set
    else:
        # If the file does not exist, create a new file and return an empty set
        with open(json_file_path, "w") as file:
            json.dump([], file)
        return set()


def send_message(group_id, message):
    """
    Send a message to a specified group.

    Args:
        group_id (int): The ID of the group.
        message (str): The message to be sent.
    """
    # URL for the API endpoint
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"

    # Payload for the API request
    payload = {
        "serviceId": "works",  # Service ID
        "channelNo": group_id,  # Group ID
        "tempMessageId": tempMessageId,  # Temporary message ID
        "caller": {
            "domainId": domainId,  # Domain ID
            "userNo": userNo,  # User number
        },
        "extras": "",  # Extra information (empty in this case)
        "content": message,  # Message content
        "type": 1,  # Message type (1 for text message)
    }

    # Send an HTTP POST request to the API endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 200:
        print("メッセージの送信に成功しました！")
    else:
        print("メッセージの送信に失敗しました。ステータスコード:", response.status_code)


def get_balance():
    # リクエストURL
    url = "https://sms-activate.org/api/api.php"

    # ヘッダー
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": 'lang=en; loyal_rank=0; isRetail=1; accept_cookie=all; g_state={"i_l":0}; _cfuvid=nLmG0DKhLH0L0BJS.lYIaH0UOfIDOca4Xlkewm3JUDo-1717303306027-0.0.1.1-604800000; PHPSESSID=8ms1kq17veme4uce1qlo13puu6; userid=10283712; sound=1; refresh_token=4b7e5d53bda85afd91ecf75a76f13015; mobile=true; session=5dda4e3cca27bb934fae1187f8485da0; cf_clearance=hhu5qu.iIcBIun4c_.KZ5qIoeKzxJCLHaooqjtqsQPQ-1717316899-1.0.1.1-l2HIFzyB6YblCdP4ZK4OkKool72TRP.9W_PdLbltqwr8I9kIvgSJ6vqEGHpFPboiWIrOn.5fmR7UqkJrWZqmhA; __cf_bm=nqTIA0RXxOdB7jg1t2Sh19uY_JO23bvPptyA2nWcqEg-1717317809-1.0.1.1-XQ1j7mkJ9VnYXjSBIRzJYKBKBg2HW6mLY3JfaGU0SGW2.GLKV59gUyon2HezEDi8NCr2f8izbc2DGNvIVcZFmg',
        "Origin": "https://sms-activate.org",
        "Referer": "https://sms-activate.org/en/freePrice",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    # ボディ
    data = {"act": "getBalance", "csrf": "a971807bd8c11545e30df1694471a489", "totals": "true"}

    # POSTリクエストの送信
    response = requests.post(url, headers=headers, data=data)

    # JSONレスポンスの解析
    json_response = response.json()

    # JSONレスポンスからbalansの値を取得
    balans_value = json_response.get("balans")

    return balans_value


# アカウントを生成する関数
def generate_account():
    url = "https://sms-activate.org/stubs/handler_hstock.php"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://sms-activate.org",
        "Referer": "https://sms-activate.org/en/freePrice",
        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": 'lang=en; loyal_rank=0; isRetail=1; accept_cookie=all; g_state={"i_l":0}; _cfuvid=nLmG0DKhLH0L0BJS.lYIaH0UOfIDOca4Xlkewm3JUDo-1717303306027-0.0.1.1-604800000; cf_clearance=E_f.t4G.P3E4hgq1ArW6A9E8kOheS4fgzYDHW0mvUtk-1717303330-1.0.1.1-hFcQJMv3lfbRbZBa3HUwvA1kO9Anp10.PGOmZ9AYBYeeiybgMKfgOaMgORLj_saYAR1zxgnz9V0Ji60nG86LGA; PHPSESSID=8ms1kq17veme4uce1qlo13puu6; userid=10283712; sound=1; session=a1d7b8964c9bd653f13d15841da0849f; refresh_token=4b7e5d53bda85afd91ecf75a76f13015; __cf_bm=KrpMzJVe_.dKyQb3eCk1pNCC1OjTltB011R.zQR_CAM-1717304213-1.0.1.1-lsy4zkB4fpHq1nNXdihijVIlqees2GnUcpcaQzx.Ub7Mur7aqRw71sP9pVdLFmnVsxoZs35Stpk5XDDngwbILA; mobile=true',
    }
    data = {"action": "buyProduct", "good_id": "37369", "csrf": "a971807bd8c11545e30df1694471a489"}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        response_json = response.json()
        mail = response_json.get("mail")
        password = unquote(response_json.get("password"))
        submail = response_json.get("submail")

        return mail, password, submail
    else:
        print(f"Failed to generate account, status code: {response.status_code}")
        return None, None, None


# ユーザーごとのアカウント生成数を記録する関数
def load_user_gen(user_id):
    file_path = f"user_{user_id}_gen.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {}


def save_user_gen(user_id, user_gen):
    file_path = f"user_{user_id}_gen.json"
    with open(file_path, "w") as f:
        json.dump(user_gen, f)


# 受信したメッセージを処理する関数
def handle_messages(messages, received_messages):
    for message in messages.get("result", []):
        try:
            message_no = message.get("messageNo")
            if message_no not in received_messages:
                user_no = message.get("userNo")
                content = f"{message.get('content')}"
                channel_type = message.get("channelType")
                channel_no = message.get("channelNo")

                if content == "!help":
                    send_message(
                        channel_no,
                        """[𝙶 - 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙶𝚎𝚗 𝙿𝚛𝚘]

𝙲𝚘𝚍𝚎𝚛 : 𝚗𝚎𝚣𝚞𝚖𝚒𝟶𝟼𝟸𝟽

@𝙽𝚎𝚣𝚞𝚖𝚒𝙿𝚛𝚘𝚓𝚎𝚌𝚝𝟸𝟶𝟸𝟺

!help / show command's

test / test command

!権限 / chek permission

!gen:{num} / Create the specified number of accounts(max 10)""",
                    )

                if content == "test":
                    print("新しいメッセージを受信しました:", content)
                    print("送信者のユーザー番号:", user_no)

                    send_message(channel_no, "ok, I'm works !!")

                if content.startswith("!gen:"):
                    if int(user_no) in owners and channel_type == 6:  # //! 10: group 6: chat
                        balance = get_balance()
                        if balance is not None:
                            if float(balance) < 10:
                                send_message(channel_no, f"残高が足りません。現在の残高:{balance}")
                            else:
                                num = int(content[5:])
                                user_id = int(user_no)  # user_noを整数型に変換
                                user_gen = load_user_gen(user_id)
                                total = user_gen.get(
                                    str(user_id), 0
                                )  # 既存の値を取得、存在しない場合はデフォルトで0を返す
                                if total + num > 10:  # //! 10 個数
                                    send_message(channel_no, "個数は10を超えることはできません。")  # //! 10 個数
                                else:
                                    user_gen[str(user_id)] = total + num  # 既存の値に新しい値を加算して保存
                                    save_user_gen(user_id, user_gen)
                                    for _ in range(num):
                                        try:
                                            mail, password, submail = generate_account()
                                            if mail and password and submail:
                                                message = f"[𝙶 - 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙶𝚎𝚗 𝙿𝚛𝚘]\n\n𝙼𝚊𝚒𝚕𝚊𝚍𝚍𝚛𝚎𝚜𝚜:\n{mail}\n\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍:\n{password}\n\n𝚂𝚞𝚋𝚖𝚊𝚒𝚕:\n{submail}"
                                                send_message(channel_no, message)
                                            else:
                                                send_message(
                                                    channel_no,
                                                    "アカウントの生成に失敗しました、メッセージの送信をスキップします。",
                                                )
                                        except Exception as e:
                                            print(f"Failed to generate account: {e}")
                                            send_message(
                                                channel_no,
                                                "アカウントの生成に失敗しました、メッセージの送信をスキップします。",
                                            )
                        else:
                            send_message(channel_no, "残高の取得に失敗しました。")
                    else:
                        send_message(channel_no, "この機能は個人チャットでのみ使用できます。")

                if content == "!権限":
                    if int(user_no) in owners:  # user_noを整数に変換して比較
                        send_message(channel_no, "[𝙶 - 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙶𝚎𝚗 𝙿𝚛𝚘]\n You are the authority✅️")
                    else:
                        send_message(channel_no, "[𝙶 - 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙶𝚎𝚗 𝙿𝚛𝚘]\n You are not an authority ❌️")

                received_messages.add(message_no)
                received_message = (message_no, channel_no, message.get("lastMessageNo"), message.get("messageTime"))
                received_messages.add(received_message)

        except Exception as e:
            print(f"Failed to handle message: {e}")

    save_received_messages(received_messages, "received_messages.json")


receive_messages(headers)
