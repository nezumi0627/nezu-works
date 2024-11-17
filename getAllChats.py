import requests


def getAllChats():
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/getVisibleUserChannelList"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": 'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; debug=false; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; _ga=GA1.2.812423193.1717075534; NEO_CHK="AAAAYTSMdT17LllIPwdDkulX48ovyMP2YjrjdMaw2G5qZswNahrAPqruOE2WF30Xf14u/zLYxNBBbK658EBw0rFmiDXHTb7rc2ttys7oCwZjJbsRGpJ3mVCu0moYT7tpfYkk4YJRR5S87o8SgseQvouGKSM="; WORKS_SES=eJwVkckBA0EIw1riZnly9l9SJgVYtqDMcE4UbGoK/dOOTI8ulW/PkdKy6NuNtkgR+PTTHEK9RXBuK0mqExqsSW7AB8CoxTUXjnaOBd8wU08hoUwWYrcmwczes9d0FxmSN1cW0dy94cYuwnDu34dcHeOkXrFd6S1chBJiCaqhs9kVmAvrpbRBrvkyTDD9vCxJZ9D0OyqtS106mu86YXnssfqJBiG5hSwe3PnwfXkHFWBLNU9WCLqTKdhqXb/2ZwB5NZjNNtZM/KGtilIqvALbfQsonOveNYFUP7rtLjCQf5OhYe3I2wA3jzB/luUu6rd8InLKvu8LNv2SvfVF/gDyoGbI; _ga_0PNBRDDHVC=GS1.1.1722931383.9.0.1722931383.0.0.0; _ga_02PY6WYJV6=GS1.1.1722930108.20.1.1722931397.0.0.0',
        "Device-Language": "ja_JP",
        "Origin": "https://talk.worksmobile.com",
        "Priority": "u=1, i",
        "Referer": "https://talk.worksmobile.com/",
        "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "Web-Device-Id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c",
        "X-Ocn": "11",
        "X-Request-Id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c-1722931397651-854-origin/v4.0",
        "X-Translate-Lang": "ja",
    }

    data = {
        "serviceId": "works",
        "userKey": {"domainId": 400486244, "userNo": 110002509263230},
        "filter": "none",
        "updatePaging": True,
        "pagingCount": 20,
        "userInfoCount": 8,
        "updateTime": 0,
        "beforeMsgTime": 0,
        "isPin": False,
        "requestAgain": False,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# 使用例
try:
    chat_data = getAllChats()
    print(chat_data)
except requests.RequestException as e:
    print(f"An error occurred: {e}")
