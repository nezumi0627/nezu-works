import requests


def quit_chat(service_id, channel_no, user_no, domain_id):
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/quit"
    headers = {
        "cache-control": "no-cache",
        "content-encoding": "gzip",
        "content-type": "application/json; charset=UTF-8",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "cookie": "language=ja_JP; LC=ja_JP; ...",  # 実際のクッキーをここに入力してください
        "origin": "https://talk.worksmobile.com",
        "referer": "https://talk.worksmobile.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "web-device-id": "110002509263230-6e047dc6-e991-e8d9-5fc7-ee6b24b2b683",
        "x-ocn": "11",
        "x-request-id": "110002509263230-6e047dc6-e991-e8d9-5fc7-ee6b24b2b683-1722493726471-61-origin/v4.0",
        "x-translate-lang": "ja",
    }
    payload = {
        "serviceId": service_id,
        "channelNo": channel_no,
        "userKey": {"userNo": user_no, "domainId": domain_id},
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Request was successful")
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None


# 使用例
response = quit_chat("works", 287878941, 110002509263230, 400486244)
print
