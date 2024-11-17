import requests
import random
import string
import time

# アカウント作成のリクエストURL
create_account_url = 'https://admin.worksmobile.com/api/Z846869/contact/adminapi/v1/users'
# 招待のリクエストURL
invite_url = 'https://talk.worksmobile.com/p/oneapp/client/chat/join'

# クッキーとヘッダーの設定
cookies = {
    "language": "ja_JP",
    "LC": "ja_JP",
    "NNB": "GN6PM456G5MGM",
    "WORKS_RE_LOC": "jp1",
    "WORKS_TE_LOC": "jp1",
    "timezone": "Asia/Tokyo",
    "TZ": "Asia/Tokyo",
    "WORKS_LOGIN_TYPE": "id",
    "WORKS_LOGIN_ID_LIST": "XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58",
    "debug": "false",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
    "WORKS_USER_ID": "6Dil8Dy3FxV0k57YgOFG_RAcr9j1zoldHweinCHDrLU",
    "WORKS_USER_DOMAIN": "gwegwegwe",
    "NEO_SES": "AAABBlXcuJa7nA8v32MV8rfBme+DdoHIEtM7eMAJnXPn716VrZmSs8PqlN7S6QQQlt0lBk9S/GKe4HgrtMEFZPAfFl172qm7qyXSNnk2gp6DWraUv9Ga47efJaXdxzxlY5uq60jRTsiRrc381nO8fxrZm/lPMqvtb6u05c2ttOToq33mxoJRQ+BfkKa+qGlAVrdRP+ERbTh8MpZYCw1YITkSkwpQqycypdkviFE9FQK0VcmxhPRVz6HnNpAcHCXzu6A4uJfF1522b+nMIQ7WG5QYgM5lVsfCcFJtGAXET/XN9ylCa0DAdBZqwnCik3z0iAWUKBAvPXk8cMpz8vz6PKLqnKpKwcR6bEBCr/atzCkyZjXu",
    "NEO_CHK": "AAAAYAnfE3EkLzeVRonMbK3Ci7OjzKO766acz7NAhqG734A/r+RJzn1eAdBtF+NAea5SNWXInGVZjCGELWtNsNFb9e8Tv7ctKDOby9txefVnc8oGEMV9hGw9aLn9PcmZv1K6Eg==",
    "WORKS_SES": "eJwVkMcRBEEIA1PCszyx+Yd0c28VEt1lhnOiYFNT6J92ZHp0qXx7jpSWRd9utEWKwKef5hDqLYJzW0lSndBgTXIDvgKMWlxz4WjnWPANM/UUEspkIXZrEszsPXtLd5EheXNlEc3dG27sIgzn/n3I1TFO6hXbld7CRSghlqAaOptdgbmwXkob5JrvhgmmH5cl6QyafkeldalLR/NdJyyPva5+oEFIbiGLB3c+fF/eQQXYUs2DFYLuZAq2Wtev/RFAXg1ms401E39oq6IvvQhneoHZCBx+TR0XZ8yI8h5jFt5Jc5NUm14t6YjTSltnpP7v+T7NjM/MDfglPc+9P+WBZoc=",
}


headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Request-Id": "110002508880628-a9c67e42-4ddd-6a86-2c0f-10ea3df335b8-1717069563465-349-origin/v4.0",
}

user_key_list = []

for _ in range(28):
    # ランダムな6桁の数字列を生成
    random_number = ''.join(random.choices(string.digits, k=6))
    # accountIdを生成
    account_id = "nezumiworks" + random_number

    # リクエストデータを作成
    payload = {
        "organizations": [
            {
                "domainId": "400456951",
                "accountId": account_id,
                "externalKey": "",
                "orgUnits": [],
                "represent": True
            }
        ],
        "name": {
            "firstName": "ねずみってじつは",
            "lastName": "れんやなんですよね"
        },
        "levelId": 230000002077154,
        "passwordCreation": "AUTO",
        "mobilePhoneCountryCode": "+81",
        "language": "ja_JP",
        "aliasEmails": [],
        "birthday": {
            "calendarType": "S",
            "content": ""
        },
        "deletedPhoto": False,
        "employmentTypeId": 0,
        "hiredDate": "",
        "i18nNames": [],
        "invitationEmail": "",
        "location": "",
        "messenger": {
            "content": "",
            "customType": "",
            "type": ""
        },
        "mobilePhone": "",
        "nickName": "",
        "password": "",
        "photoPath": "",
        "privateEmail": "",
        "relations": [],
        "task": "",
        "workPhone": "",
        "activationDate": "",
        "employeeNumber": ""
    }

    # アカウント作成のリクエストを送信
    response_create_account = requests.post(create_account_url, headers=headers, cookies=cookies, json=payload)

    # レスポンスを確認
    print("Account Creation Status Code:", response_create_account.status_code)
    print("Account Creation Response:", response_create_account.json())

    # アカウント作成のレスポンスから必要な情報を取得
    if response_create_account.status_code == 201:
        user_no = response_create_account.json()['id']
        user_key_list.append({
            "domainId": 400456951,
            "userNo": user_no
        })
        print("User No:", user_no)
        time.sleep(0.4)
    else:
        print("Failed to create account")

# 招待のリクエストデータを作成
invite_payload = {
    "channelNo": 276496885,
    "channelType": 10,
    "botNoList": [],
    "userKeyList": user_key_list,
    "dlNoList": [],
    "groupNoList": [],
    "requestService": "",
    "description": "undefined",
    "inviter": {
        "domainId": 400456951,
        "userNo": 110002508970551
    }
}

# 招待のリクエストを送信
response_invite = requests.post(invite_url, headers=headers, cookies=cookies, json=invite_payload)

# 招待のレスポンスを確認
print("Invitation Status Code:", response_invite.status_code)
print("Invitation Response:", response_invite.json())
