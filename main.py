import requests

# セッションを開始
session = requests.Session()

# メインリクエストのURLとヘッダー
url = "https://sms-activate.org/api/api.php"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://sms-activate.org",
    "Referer": "https://sms-activate.org/en/freePrice",
    "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# クッキーを設定
cookies = {
    "lang": "en",
    "loyal_rank": "0",
    "isRetail": "1",
    "accept_cookie": "all",
    "g_state": '{"i_l":0}',
    "desktop_download_passed": "1",
    "sound": "1",
    "PHPSESSID": "04da4u162ijajujkmnm50va41k",
    "userid": "10285687",
    "session": "34c247e19c79d4b3794d4b8c5d85d8b8",
    "refresh_token": "66c91b3e762d1decfd791940e08d5594",
    "__cf_bm": "SuMc67QwmuKS7OdGzPP2qzMUH3uRLZxNLjIw5nJ1Vd4-1717323850-1.0.1.1-BbifRv8uIzfkDS8O5ciSHe2IrGwWS1aePLKk8rHe0MPE940ky3NR_QpekwsQ27Mz56p255_CVN3gUBNMuF9JBg",
    "_cfuvid": "NKEIf5qYjmtZT0uqFXlzkUWKfkQACnDGXNIY7BU8qgM-1717323850629-0.0.1.1-604800000",
    "mobile": "false",
    "cf_clearance": "415LML1lXp6dHIXI0xtrp5rUbGLMSO0Pw4jZm4yc0OY-1717324041-1.0.1.1-kRjQ1b5Gj065M5o27Gx4j3cuEYEB462DiOudkae7Uy7tVGRWkOvtsyPIAiCVzeQo2HQNNJdZgxF3aIwO_65alw"
}

# メインリクエストのデータ
data = {
    "action": "buyProduct",
    "good_id": "37369",
    "csrf": "9c10dc6d01b4f81387353fb28f51ee8f"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.status_code)
print(response.text)
