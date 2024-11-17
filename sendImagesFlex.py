import requests

domainId = 400486244
userNo = 110002509263230
tempMessageId = 686274530


def send_message(group_id):
    """
    Send a message to a specified group.

    Args:
        group_id (int): The ID of the group.
        message (str): The message to be sent.
    """
    # URL for the API endpoint
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"
    headers = {
        "cache-control": "no-cache",
        "content-encoding": "gzip",
        "content-type": "application/json; charset=UTF-8",
        "date": "Tue, 06 Aug 2024 04:38:12 GMT",
        "server": "openresty",
        "session-id": "qtgYTU8tTPuY1dOqod5UoQ:jvapi148.oneapp",
        "strict-transport-security": "max-age=63072000; includeSubdomains; preload",
        "x-csid": "qtgYTU8tTPuY1dOqod5UoQ",
        "x-time": "0.026",
        "x-user-domain": "400486244",
        "x-user-email": "neko3desu4ne@nezumouse3",
        "x-user-no": "110002509263230",
        "x-user-tenant": "400486244",
        "x-xss-protection": "1; mode=block",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "content-length": "378",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "cookie": (
            "language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; "
            "NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; "
            "timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; "
            "WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; "
            "_uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; "
            "_gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; "
            "_ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; "
            "_ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; "
            "_ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; "
            "NEO_SES=AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/"
            "Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/"
            "glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40=; "
            "NEO_CHK=AAAAYEJQbAmxK6uI+ldJAuhNVDVpZMGfGOSh5BBE0/5+Ljtr2ivCuqYEyGf14IYDmVkEnurz0xHqPhiVULEyRHhtHOv+ygKvq4hxtWsa2cBRE+m945cn3NCnEf5+smMAThAaNg==; "
            "WORKS_SES=eJwNkLkBwEAIw1biJ5S8+4+UKylsWZQZzomCTU2hf9qR6dGl8u05UloWfbvRFikCn36aQ6i3CM5tJUl1QoM1yQ34CjBqcc2Fo51jwTfM1FNIKJOF2K1JMLP37JHuIkPy5soimrs33NhFGM79+5CrY5zUK7YrvYWLUEIsQTV0NrsCc2G9lDbINV+GCaaflyXpDJp+R6V1qUtH810nLI+9rn6iQUhuIYsHdz58X95BBdhSzZMVgu5kCrZa16/9GUBeDWazjTUTf2iropQKD2C7bwGFc937JpDqR7fd1h7vinT7XvkZPtNoCM4qqeZPPuITPGUDRXyLF+QG5rEBf+noZj4=; "
            "debug=false; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; _gat_UA-110924794-12=1; "
            "_gat_UA-217420925-6=1; _ga=GA1.2.812423193.1717075534; _ga_0PNBRDDHVC=GS1.1.1722919030.7.1.1722919075.0.0.0; "
            "_gat_UA-217420925-5=1; _ga_02PY6WYJV6=GS1.1.1722919002.18.1.1722919084.0.0.0"
        ),
        "device-language": "ja_JP",
        "origin": "https://talk.worksmobile.com",
        "priority": "u=1, i",
        "referer": "https://talk.worksmobile.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "web-device-id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c",
        "x-ocn": "11",
        "x-request-id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c-1722919089376-722-origin/v4.0",
        "x-translate-lang": "ja",
    }

    # Payload for the API request
    payload = {
        "serviceId": "works",  # Service ID
        "channelNo": group_id,  # Group ID
        "tempMessageId": tempMessageId,  # Temporary message ID
        "caller": {"domainId": domainId, "userNo": userNo},  # Domain ID  # User number
        "extras": r'{"columns":[{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_01_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_01_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_01_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_01_value.png"}},"action":{}},{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_02_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_02_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_02_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_02_value.png"}},"action":{}},{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_03_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_03_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_03_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_03_value.png"}},"action":{}}]}',  # Extra information (empty in this case)
        "content": "a",  # Message content
        "type": 98,  # Message type (1 for text message)
    }

    # Send an HTTP POST request to the API endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 200:
        print("メッセージの送信に成功しました！")
    else:
        print("メッセージの送信に失敗しました。ステータスコード:", response.status_code)


send_message(288601233)

# {
#     "code": 200,
#     "message": "OK",
#     "result": {
#         "messageId": 0,
#         "channelNo": 288601233,
#         "writerId": "110002509263230",
#         "userNo": 110002509263230,
#         "botNo": 0,
#         "messageNo": 1,
#         "content": "",
#         "memberCount": 2,
#         "messageTypeCode": 27,
#         "messageStatusType": "NORMAL",
#         "messageStatusTypeCode": 0,
#         "extras": '{"columns":[{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_01_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_01_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_01_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_01_value.png"}},"action":{}},{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_02_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_02_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_02_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_02_value.png"}},"action":{}},{"image":{"url":{"default":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_03_value.png","en":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/EN_03_value.png","ja":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/JP_03_value.png","ko":"https:\/\/static.worksmobile.net\/static\/wm\/rssbot\/KR_03_value.png"}},"action":{}}]}',
#         "tid": 190893660,
#         "createTime": 1722919092260,
#         "updateTime": 1722919092260,
#     },
# }
