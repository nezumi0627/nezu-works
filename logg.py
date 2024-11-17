import json

import requests


def send_post_request():
    url = "https://notify.worksmobile.com/p/nelo/_store"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Cookie": "language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; _ga_0PNBRDDHVC=GS1.1.1722931383.9.1.1722933481.0.0.0; NEO_SES=AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40=; NEO_CHK=AAAAX69ba3YR1Cp9d+LALgPgRWI+GDmEhG3XjDDN0MOOfYqhKx6Er/Ho7Ra3Vb2gePIXEmmRaSfknW32hZEzr01WLZjnhc32iwVm0u2S7ThrdXt5rXEpJ4/KPxT6TIruAHelIg==; WORKS_SES=eJwNkMcBwEAMwlZyd/x03X+k3AAIRJnhnCjY1BT6px2ZHl0q354jpWXRtxttkSLw6ac5hHqL4NxWklQnNFiT3IAPgFGLay4c7RwLvmGmnkJCmSzEbk2Cmb1nr+kuMiRvriyiuXvDjV2E4dy/D7k6xkm9YrvSW7gIJcQSVENnsyswF9ZLaYNc82WYYPp5WZLOoOl3VFqXunQ033XC8thj9RMNQnILWTy48+H78g4qwJZqnqwQdCdTsNW6fu3PAPJqMJttrJn4Q1sVpVR4Bbb7FlA41703gVQ/un2YO7r6Jh/GtkcidzqxfA3b+M3XC0Q2vIm3Dd73nE/MsSe+HwdqZtE=; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en; _ga_02PY6WYJV6=GS1.1.1723026915.25.0.1723026917.0.0.0; _ga=GA1.2.812423193.1717075534",
        "Origin": "https://notify.worksmobile.com",
        "Referer": "https://notify.worksmobile.com/center/",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "projectName": "works-notify-web",
        "projectVersion": "4.0.0",
        "body": "bee.js",
        "host": "script",
        "logLevel": "info",
        "logType": "json",
        "message": "mqtt.notification",
        "phase": "real",
        "contactNo": 110002509263230,
        "domainId": 400486244,
        "product": "LINE_WORKS",
        "service": "message",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "payload": {
            "aBadge": 0,
            "badge": 1855,
            "cBadge": 1855,
            "domain_id": 400486244,
            # "hBadge": 3,
            # "mBadge": 0,
            # "nType": 41,
            # "ocn": 0,
            # "sType": 2,
            "token": "110002509263230",
            "userNo": 110002509263230,
            "wpaBadge": 0,
        },
    }

    response = requests.post(url, headers=headers, json=data)
    return response


# 使用例
response = send_post_request()
print(response.status_code)
print(response.json())
