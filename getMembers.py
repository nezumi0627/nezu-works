import requests

url = "https://notify.worksmobile.com/p/nelo/_store"
headers = {
    "authority": "notify.worksmobile.com",
    "method": "POST",
    "path": "/p/nelo/_store",
    "scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://notify.worksmobile.com",
    "Referer": "https://notify.worksmobile.com/center/",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Cookie": 'language=ja_JP; LC=ja_JP; NNB=HAYYJZ2FF3DWM; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=YLg73AUFd_vD6iMx8julXzisq_bKrwo8TR6YgnvCASA; WORKS_USER_DOMAIN=sugiwaranonono; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOW1155nwmyMMjx_ctNRz_eH-EIcN5JO3YaF_zrIMaKDNiAnXDmXx2QUHzu5gZObvcjHd5xJgTtP3ULOzuoZuGAUsH1HRz5RkJZk2A2nRcFuBMb_5H15Z-ip_FzD7s1DOffTynJTTsRlrGm7PQkUJx7OX9HwllvDa5h0fxtcDOod2bHSYzROYdVOq6Xpis0E-UCrnT4Ye9TTAlP1fEahAQO06g07KHeYHApiuUKoKrErok7iaGOhR_J1BpU0gSYHQL99Ga85947xCfMY7WX4BqHHpyXMVhREENXWKw5Au91w4LZ2Em10pKKnYswaaQdIr0b52AEIGOzpvylKt9vT4lIJ076Bts8yLhct0ijygCGux3pL1PM76xGDvm3KRmQdZ7w; NEO_SES="AAABNRCm5x0efih8dieG71m0aFYFWcH3ZK7yWhWjQrTKh+IjAQRqJNmmqImxm6725tbPS/rs7yXnlE/TqF+VV7VJ9iekkXOL7d6NbzRi1yBaQi0z6zmd9GSmEMctQ04wlbZTdbP13+M3zqGlWKnoz34qkEmO476QABB0tuPHnJOLajORwzLuxQAxuioT9SL99ypi0xzB5k4rFAxRTKIvolmwQ5orEgIsW7cqsKktXyTuJc6SSoUOr/cLDPAw5JY73JMdKWm6+XaN0K0FsMMV+3JepC/xPIiDg3FHNdA0RKJDSI21V03WkNAPrKIH80ZSDPSplFRJTROiSCzbHQtzfy7lYakkSASog1b0uWTgnwFzK7lx6FacZF5h2XhrHM1zzAzFEbhHjSX8otYYj8jbmo4KAAxpWfYD+49I1/+0XxeoU9iy"; NEO_CHK="AAAAYbYLKajWhVHu04TgVWFR2Al/OJVJmXvrXbgfucSiWUQUu2p3WeQ/PKGh60HZPk91fJ+rZKHvf41dCqflArUF2r4yXp13bb0cmqiQaagrV51SlCwXzsUJ61bpefLFYz1Fa9jv4ckF38M1LGcadDaTISE="; WORKS_SES=eJwVkEcBA0EMxCi5e/105Q8pFwBTpDLDOVGwqSn0px2ZHl0qb8+R0rLo7UZbpAg8fZpDqLcIzm0lSXVCgzXJDfgVYNTimgtHO8eCb5ipp5BQJguxW5NgZu/Zt3QXGZI3VxbR3L3hxi7CcO7vIVfHOKlXbFd6CxehhFiCauhsdgXmwnopbZBrfhkmmP64LEln0PQdldalLh3Nu05YHvu6+gMNQnILWTy48+F7eQcVYEs1H6wQdCdTsNW6vvaPAPJqMJttrJn4oa2KHnusFuzq58z7xc5zeDBvNGgPYJ+T5CYRp/OquRWDCuCnej/3+cl1do0/CtVb0f3u1Xj4D+PKZhE=',
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
    "contactNo": 110002509337378,
    "domainId": 400495509,
    "product": "LINE_WORKS",
    "service": "message",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "payload": {
        "aBadge": 0,
        "badge": 3,
        "botInfo": "",
        "cBadge": 3,
        "chNo": 291108766,
        "chPhotoPath": "",
        "chTitle": "ミクの権限者たち(雑談まる)",
        "chType": 10,
        # "createTime": 1724596439119,
        "domain_id": 400495509,
        "extras": "",
        "fromPhotoHash": "5993119b887453034a0050e2e8c0966c",
        "fromUserNo": 902100014853844,
        "hBadge": 3,
        "loc-args0": "まぐ",
        "loc-args1": "@もやしれん @K⃠.Y⃠ \nhttps://github.com/MocA-Love/miq-api-doc/releases/tag/v1.3.5\n\nスタンプ関連修正済",
        "loc-key": "REV_MSG",
        "mBadge": 0,
        "messageNo": 785,
        "nType": 1,
        # "notification-id": "msg.AAAAAAAAAACe91kRAAAAABEDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "ocn": 0,
        "sType": 2,
        "token": "110002509337378",
        "userNo": 110002509337378,
        "wpaBadge": 0,
    },
}

response = requests.post(url, headers=headers, json=data)

print(f"Response Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
