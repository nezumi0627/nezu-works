import requests
import random
import string


cookies = {
    "language": "ja_JP",
    "LC": "ja_JP",
    "_mkto_trk": "id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520",
    "NNB": "MVJDTEKMPZMGM",
    "_gcl_au": "1.1.357572222.1717075534",
    "_yjsu_yjad": "1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6",
    "timezone": "Asia/Tokyo",
    "TZ": "Asia/Tokyo",
    "_gid": "GA1.2.543969814.1717326065",
    "_ga_0PNBRDDHVC": "GS1.1.1717326064.2.0.1717326065.0.0.0",
    "WORKS_RE_LOC": "jp2",
    "WORKS_TE_LOC": "jp2",
    "WORKS_USER_ID": "hmfSevSLSuz_ftXiap9osMCYrrrAyCviVSJ7DrEXgH8",
    "WORKS_USER_DOMAIN": "wfeweg",
    "NEO_SES": "\"AAABE+1tBPcqb47sWVlQ5jxumq3G1y/1wWbutlTzxOj6s3gerbM6SMxqLux1TYoBsQ3e/PKdfSaMT5Q09x2ZNmF+JFCuHiBRRjgvMw9/3dOS0ov2xz0+FCRj3Xvasr4YW08sHu0LCRoeiympwgxtkhTJOTy68LnUAW3ChN2XDQCuvnTAHy8sBt18oquqmelEY9wLyflF7L9IAunYLM85gFOFBKkhipZW7NpZ7br0FUu5r8pRsYkpKqnGpJlx/M0xe1FujN0L+wZdzVk7UHdhydTSXOxskkKKu+I7MlNKIfY9dZ9riaxVEELbHPL+SxQ7fIHJpba5O9BEkh1Rs2XhhHiZetRcWFjvPYCUkOg+kWGL1lm0RnucNWqRzL3EQbK7htjMfQ==\"",
    "NEO_CHK": "\"AAAAX5/pyTNPV5Q1rSJiNysdnquAjbsOZvzC5R6HbNieWilPmvBNL5ws7rqW8WqiVNx+BEQYdtfdbqlVUYIdfBCPSu4AZ6xRtJgJ3jrXEhFAkZ5J7dZ6Og9X+0II3gpGcMPzcg==\"",
    "_uetsid": "b15726a020cf11efb92f41f27931a434",
    "_uetvid": "1895b0d01e8811efa4551b9a59d68d81",
    "_ga_LG7FMZLY53": "GS1.1.1717330392.3.1.1717330448.4.0.0",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "en",
    "_ga_03NNQM7KD0": "GS1.1.1717330452.2.1.1717330456.0.0.0",
    "_ga_02PY6WYJV6": "GS1.1.1717330459.2.0.1717330465.0.0.0",
    "_ga": "GA1.2.812423193.1717075534",
    "WORKS_SES": "eJwV0LkRBEEIA8CU+FlM3vxDujkPB6laZYZzomBTU+ifdmR6dKl8e46UlkXfbrRFisCnn+YQ6i2Cc1tJUp3QYE1yA74AjFpcc+Fo51jwDTP1FBLKZCF2axLM7D17TXeRIXlzZRHN3Rtu7CIM5/59yNUxTuoV25XewkUoIZagGjqbXYG5sF5KG+Sa74cJpp/LknQGTb+j0rrUpaP5rhOWx15WP2gQklvI4sGdD9+Xd1ABtlTzsELQnUzBVnxa+Mr73j0AOIl4n8/dCHYaduyogk88OwIluFs6DubRK222tZsp4bUR+4KSHjljuf8rUjSm+gHcW23rmUZ8v0SY+wHmaWaJ; _gat_UA-217420925-5=1; _ga_02PY6WYJV6=GS1.1.1717330459.2.1.1717332955.0.0.0"
}
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Request-Id": "110002508880628-a9c67e42-4ddd-6a86-2c0f-10ea3df335b8-1717069563465-349-origin/v4.0",
}

# ランダムな6桁の数字列を生成
random_number = ''.join(random.choices(string.digits, k=6))
# accountIdを生成
account_id = "nb" + random_number

# リクエストデータを作成
payload = {
    "organizations": [
        {
            "domainId": "400445199",
            "accountId": account_id,
            "externalKey": "",
            "orgUnits": [],
            "represent": True
        }
    ],
    "name": {
        "firstName": "NBOT",
        "lastName": "BOT" + random_number
    },
    "levelId": 230000002028444,
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

# リクエストを送信
response = requests.post('https://admin.worksmobile.com/api/Z846869/contact/adminapi/v1/users', headers=headers, cookies=cookies, json=payload)

# レスポンスを表示
print(response.status_code)  # ステータスコード
print(response.json())       # レスポンスデータ
