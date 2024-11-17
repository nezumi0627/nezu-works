import requests
import json

# リクエストヘッダー
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ja',
    'Cookie': "WORKS_LOGIN_TYPE=id;TZ=Asia/Tokyo;timezone=Asia/Tokyo;WORKS_TE_LOC=jp1;language=ja_JP;WORKS_RE_LOC=jp1;NEO_SES=AAABH2UgiZ6DrzBig/Ic7y6CFBa2N2twPmaugHMKzlx7hzisy75hEF5Le980ts0Z7pV/LMYuiFMQrJkp+3mZH1I0s9k9QFXJ9GMeFN0HEpdSwNyGod/tSaH481XKrj4IeaLVNr9sW/llY8qcgrgbzFitLW//My9K4QDI56b0LnsSTlkd0HtkSqE7bkbETYtqnl4GbJGxLVZLTa8b7PSAgyrmKO0J+/sc22+BCm9AfLuB+pXE2iUns4ykWDq1PokMI18ZbCDUuqweLRlVnJ68T3aZrRAdNWD8wx5Zc6s9SSoWYve7QmQ4YcRy/PgymynzG8t4csamzVmrrLKEVzo/KAkgk3EMrCgzHfxKON0Asdhnq52aRNVwRejHbPcwKy8KpA9bcQ==;WORKS_SES=eJwVULcRBEEIawm3mJDD9F/S85lmZJCg9q2E4VZCKfIJQjINGVzYzc7QJ4Yi74T61EMkIlM0Oow1zRT9lEa4+nWtVx6BBbNh8X1QMZxT/DUYfsi5inSpo4ya0wUGT/yjJ9Udan0i+QZkljMEqdvCgKI8y004nkvTiw0Xfp36eUMiSJ0LdHD8yrw/UPev1K86M/tGePKyS2rbpbYytOG5O0u3EeA8RMgzn/gT8ldzVzk+i3RrknZ1zoz12EdqtNVH+nWkfA5lwZEGfcDn3WdMbhRr7fY3TPklLO+0/wCeNFd5;WORKS_USER_DOMAIN=mouse;WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw;LC=ja_JP;WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q",
    'Device-Language': 'ja_JP',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

# リクエストを送信
response = requests.get('https://talk.worksmobile.com/p/contact/v3/domain/contacts/my', headers=headers)

# ステータスコードをチェック
if response.status_code == 200:
    # 結果をJSONファイルに保存
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    print('結果がresult.jsonに保存されました。')
else:
    print('リクエストが失敗しました。ステータスコード:', response.status_code)
