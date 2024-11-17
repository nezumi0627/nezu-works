import requests
import uuid

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
    'NEO_SES': 'AAABKDkfjNzTqOjy6/wC7W/Z92PdiuBaFVLt0jOayzfWxKIODBH40sEiwpJfgH/S5LvK/2KaViXrkPLyvBr54XUHeMa9bspQDcVVUI3mIwHQouv0N6U2RpxyIms3ueCyTY727NaPpXByQpcHTiHCxdaTIm9T77aSxATi+BkpCGcGniW3a6rROmlDfUNsmiCnq6jM2mQlh6JohC1lSefR2hC5g7KZjBnaz7fLf0RNUoYcWu9uGmYQh1Jh9wSt4JjoMI2KNWtYsFZhcQlz1rS4WTLlQNzgU6QUZOCQQLvLfTHhB7y4fMIV2V5F+Ssdy3XROU+loX5cqZc0QQQMMtalhQhS0dna4u+/uuHquoTp/U+bztlcvTHuaGiewP92V34SFlW5NTz/Z7UMwgf19C9/ekzEAoM=',
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Request-Id": "110002508880628-a9c67e42-4ddd-6a86-2c0f-10ea3df335b8-1717069563465-349-origin/v4.0",
}

for i in range(1, 11):
    payload = {
        "channelNo": 0,
        "channelType": 7,
        "botNoList": [],
        "userKeyList": [
            {
                "domainId": 0,
                "userNo": 913000041624790
            },
            {
                "domainId": 0,
                "userNo": 913000039557226
            }
        ],
        "dlNoList": [],
        "groupNoList": [],
        "requestService": "",
        "title": f"{i}",
        "photoPath": "",
        "description": "",
        "sendExcludeMemberSystemMsg": True,
        "inviter": {
            "domainId": 400445199,
            "userNo": 110002508880628
        }
    }

    response = requests.post('https://talk.worksmobile.com/p/oneapp/client/chat/join', headers=headers, cookies=cookies, json=payload)

    print(f"{i}個目のグループを作成しました。")

