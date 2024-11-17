import requests


def searchSameChannel():
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/recommendChannel"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "content-type": "application/json;charset=UTF-8",
        "cookie": (
            "language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; "
            "_yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; "
            "WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; "
            "_gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; "
            "_ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; "
            "_ga_0PNBRDDHVC=GS1.1.1722931383.9.1.1722933481.0.0.0; NEO_SES=AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40=; "
            "NEO_CHK=AAAAYI8EXLta4Ri+spn19XOi0ssJkDCRT4k/E/QT+MhwYC47+AXxHYF4kUBSb2a92SHC08AdqawgZr4b1UBnNdTXicG66kNz4Nq2bYEXpO/SogJYggCgpKUuk1gmXY9Gbyikzg==; WORKS_SES=eJwNkNsBAEEEA1vydj6x9F/SKSDJTMoM34qCvXqF/mlHpkeXyjfrSGlZ9M1EW6QIfPppPkLdQXBuK0mqFXpYL7kBrwCjBsdcONo5BnzCTD2FhDJZiN2aBDN71m5pNzIk921ZRHP3hBu7CMO6fx9ydTwn9YrpSm/hIpQQS1ANfZNdgTkwXkoT5JqXYYLX52VJ+h6afkultalDS+/bThh+dl19okFIbiGDC7v+eL/chQqwoXonKwTdyRRsNa5f+xlAbj3MZnvWTPyhjYpSKtyAzRwBhXPtvQmk+tFON8JlPL57P9dC4ePSfn0Ofrk73/MGIK+eJGYg2P3A0OId/A/8pmbG; debug=false; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; "
            "_ga_02PY6WYJV6=GS1.1.1722958144.23.0.1722958144.0.0.0; _ga=GA1.2.812423193.1717075534; _gat_UA-217420925-5=1"
        ),
        "device-language": "ja_JP",
        "origin": "https://talk.worksmobile.com",
        "referer": "https://talk.worksmobile.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        ),
        "web-device-id": "110002509263230-2a21b2a2-f713-c0aa-d4ee-a99a9308382b",
        "x-ocn": "11",
        # "x-request-id": "110002509263230-2a21b2a2-f713-c0aa-d4ee-a99a9308382b-1722958188235-514-origin/v4.0",
        "x-translate-lang": "ja",
    }
    payload = {
        "userNoList": [],
        "externalUserNoList": [913000043047576, 913000041288116],
        "botNoList": [],
        "dlNoList": [],
        "groupNoList": [],
        "start": 0,
        "count": 30,
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data.get('code') == 200:
            channel_list = data.get('channelList', [])
            for channel in channel_list:
                print(f"グループ名: {channel['title']}")
                print(f"グループID: {channel['channelNo']}")
                print(f"参加人数: {channel['memberCount']}")
                print('----------------------------')
        else:
            print(f"Error: {data.get('message')}")
    else:
        print(f"HTTP Error: {response.status_code}")

searchSameChannel()