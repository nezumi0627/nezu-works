import json
import os
import requests

owners = [913000041624790, 913000041325191]  # ユーザー番号を整数に変換

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/json;charset=UTF-8",
    "Device-Language": "ja_JP",
    "Origin": "https://talk.worksmobile.com",
    "Referer": "https://talk.worksmobile.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Web-Device-Id": "110002508880628-fcdacea1-68c6-5b8b-7d2e-e121557cfa40",
    "X-Ocn": "11",
    "X-Request-Id": "110002508880628-fcdacea1-68c6-5b8b-7d2e-e121557cfa40-1717305726407-480-origin/v4.0",
    "X-Translate-Lang": "ja"
}

cookies = {
    'language': 'ja_JP',
    'LC': 'ja_JP',
    'NNB': 'GN6PM456G5MGM',
    'WORKS_RE_LOC': 'jp1',
    'WORKS_TE_LOC': 'jp1',
    'timezone': 'Asia/Tokyo',
    'TZ': 'Asia/Tokyo',
    'WORKS_LOGIN_TYPE': 'id',
    'WORKS_USER_DOMAIN': 'agroupofmice',
    'WORKS_USER_ID': 'LWxTHdDaKJ7MW-Edx8ADH66cCwHqJpX8m3zY-2dmW7o',
    'NEO_SES': 'AAABJYbong3sQfy23Bzgm3tmECLdNqLSVVNnXdHO0itAMNY+/NJQLQTMMy6X5X+C17ICct4VI3ZeQYwJ9flEiGT4V4BOgBVdaZ1jTkltwjga/olAOELvG/nzIgH4eO76iXe4y5DyCZfblXX/v60t/HCIP41nYLB01WrVcqW6P84qUyR0J0Sg3IC8UsKqppi2WEUr1wDMio0pI5R0/lQD4GSKM+DxtTPep/dMfdCaVlcZwyZvVB9xXKpX5DE436j3+lOdsCrds2M5ZXCnBGq0g0ACBKl5PZX3pgXcJhuRfH0wWaQhT8q0Wv3s5rBKcUTzB022GY4yfWBGew70vk/xztF+V/JXdzL3ywosqe752zxX+V6mk9b046vz9X0SKhNY4uiJFI5cX1czEvsJRrN3mZmODHI=',
}

def receive_messages(headers, cookies):
    json_file_path = "received_messages.json"
    received_messages = load_received_messages(json_file_path)

    url = "https://talk.worksmobile.com/p/oneapp/client/chat/syncUserChannelList"
    payload = {
        "serviceId": "works",
        "userKey": {
            "domainId": 400445199,
            "userNo": 110002508880628
        },
        "filter": "none",
        "updatePaging": True,
        "pagingCount": 50,
        "userInfoCount": 8,
        "updateTime": 1717305628181,
        "beforeMsgTime": 0,
        "isPin": True,
        "requestAgain": False
    }

    try:
        while True:
            response = requests.post(url, json=payload, headers=headers, cookies=cookies, timeout=30)

            if response.status_code == 200:
                handle_messages(response.json(), received_messages, headers, cookies)
    except Exception as e:
        print("エラー:", e)

def save_received_messages(received_messages, json_file_path):
    with open(json_file_path, "w") as file:
        json.dump(list(received_messages), file)

def load_received_messages(json_file_path):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return {tuple(item) if isinstance(item, list) else item for item in data}
            else:
                print("警告: JSONファイルのデータ形式が予期しないものです。")
                return set()
    else:
        return set()

def send_message(group_id, message, headers, cookies):
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"

    payload = {
        "serviceId": "works",
        "channelNo": group_id,
        "tempMessageId": 725703460,
        "caller": {
            "domainId": 400445199,
            "userNo": 110002508880628
        },
        "extras": "",
        "content": message,
        "type": 1
    }

    response = requests.post(url, headers=headers, cookies=cookies, json=payload)

    if response.status_code == 200:
        print("メッセージの送信に成功しました！")
    else:
        print("メッセージの送信に失敗しました。ステータスコード:", response.status_code)


def handle_messages(messages, received_messages, headers, cookies):
    for message in messages.get('result', []):
        message_no = message.get('messageNo')
        if message_no not in received_messages:
            user_no = message.get('userNo')
            content = message.get('content')

            if content == "!test":
                print("新しいメッセージを受信しました:", content)
                print("送信者のユーザー番号:", user_no)

                send_message(message.get('channelNo'), "ok, I'm works !!", headers, cookies)

            if content == "!権限":
                if int(user_no) in owners:  # user_noを整数に変換して比較
                    send_message(message.get('channelNo'), "あなたは権限者です", headers, cookies)
                else:
                    send_message(message.get('channelNo'), "あなたは権限者ではありません", headers, cookies)

            received_messages.add(message_no)
            received_message = (message_no, message.get('channelNo'), message.get('lastMessageNo'), message.get('messageTime'))
            received_messages.add(received_message)

    save_received_messages(received_messages, "received_messages.json")

receive_messages(headers, cookies)
