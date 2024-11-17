import requests
import json
import os

url = "https://talk.worksmobile.com/p/oneapp/client/chat/syncUserChannelList"

headers = {
    "Cache-Control": "no-cache",
    "Content-Encoding": "gzip",
    "Content-Type": "application/json; charset=UTF-8",
    "Session-Id": "eCBNmJK6RmyepJRQxst0mg:jvapi110.oneapp",
    "Strict-Transport-Security": "max-age=63072000; includeSubdomains; preload",
    "X-Csid": "eCBNmJK6RmyepJRQxst0mg",
    "X-Time": "0.025",
    "X-User-Domain": "400460495",
    "X-User-Email": "nezumi0627@mouse",
    "X-User-No": "110002509004447",
    "X-User-Tenant": "400460495",
    "X-Xss-Protection": "1; mode=block",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Length": "229",
    "Cookie": "language=ja_JP; LC=ja_JP; NNB=GN6PM456G5MGM; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58; debug=false; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; WORKS_USER_DOMAIN=mouse; NEO_SES=AAABH1FJB/ckmrAoSNzZ1O74FkjHFGwC3F8kE6YpGXtO90xqck79ZDTfkiWUN2OijLUWUpwgYkYvdlRRDWQ9KQhQnVgVySvE655ykrUhNYapn7smYj4PX4DZzMS2PQSVOlarPCqQV4r2AncKq+uJP94uYsflP8Tp1/bjMGAZTSlJpEsxhQAD5lrh3n0Bzxp3vSGVkBb6uZwlIldm1EcXX5qf/FE5NEdKirNPmBXF27o8ViuyOZPdeFVJLp/Y851Q5gdtBqr8NHQA3H1ShXcuDum/3Ao+cC598mcCL217NAdMImbhw7pXsMPsDRyTWGWAg+ikQS7OY2t1CnfT6nLnr7Zy673F67SafVj0uTudfFt5VJX8B/mRZtE=",
    "Device-Language": "ja_JP",
    "Origin": "https://talk.worksmobile.com",
    "Priority": "u=1, i",
    "Referer": "https://talk.worksmobile.com/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Web-Device-Id": "110002509004447-c53772d8-7221-8cc2-e059-24f558c2ebc1",
    "X-Ocn": "11",
    "X-Request-Id": "110002509004447-c53772d8-7221-8cc2-e059-24f558c2ebc1-1718447428733-142-origin/v4.0",
    "X-Translate-Lang": "ja"
}

data = {
    "serviceId": "works",
    "userKey": {
        "domainId": "400460495",  # 文字列として指定
        "userNo": "110002509004447"  # 文字列として指定
    },
    "filter": "none",
    "updatePaging": True,
    "pagingCount": 50,
    "userInfoCount": 8,
    "updateTime": 1718447415405,
    "beforeMsgTime": 0,
    "isPin": True,
    "requestAgain": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 確認用にステータスコードとレスポンスを表示
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200:
    result = response.json()
    full_url = None
    for message in result.get("result", []):
        if message["messageTypeCode"] == 11:
            extras = json.loads(message["extras"])
            resource_path = extras.get("resourcepath")
            if resource_path:
                full_url = "https://storage.worksmobile.com" + resource_path.replace('\\', '')
                break

    if full_url:
        print(f"Full URL: {full_url}")
        image_response = requests.get(full_url, headers=headers)  # 認証ヘッダーを追加
        if image_response.status_code == 200:
            image_path = os.path.join(os.getcwd(), "./images/downloaded_image.jpg")
            with open(image_path, 'wb') as f:
                f.write(image_response.content)
            print(f"Image downloaded and saved as {image_path}")
        else:
            print(f"Failed to download image, status code: {image_response.status_code}")
    else:
        print("No resource path found")
else:
    print(f"Failed to get response, status code: {response.status_code}")
