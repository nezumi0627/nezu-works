import requests


def get_read_infos(channel_no, service_id):
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/getReadInfos"
    headers = {
        "cache-control": "no-cache",
        "client-ip": "59.170.183.99",
        "content-encoding": "gzip",
        "content-type": "application/json; charset=UTF-8",
        "date": "Wed, 07 Aug 2024 13:45:57 GMT",
        "server": "openresty",
        "session-id": "bXI4pjOjQT+T40AKE6vHyA:jvapi164.oneapp",
        "strict-transport-security": "max-age=63072000; includeSubdomains; preload",
        "x-csid": "bXI4pjOjQT+T40AKE6vHyA",
        "x-time": "0.010",
        "x-user-domain": "400486244",
        "x-user-email": "neko3desu4ne@nezumouse3",
        "x-user-no": "110002509263230",
        "x-user-tenant": "400486244",
        "x-xss-protection": "1; mode=block",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en-US;q=0.9,en;q=0.8",
        "cookie": "language=ja_JP; LC=ja_JP; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; WORKS_LOGIN_ND=Y; NEO_SES=AAABMTpiM9SrmYd67xKCptJnYY0Ek2DDnVjVVWwFiFLqx7N3EHgkgS9rs+M2Ee8cVd3tn+o0LoLd/+HdkqjsVNuRipYeriSbFOrUjPMY48iO9trfJ9Kb75Evs3HkYFR5lq3bxoU+bcdu9bT74UbBCAR57QokfZF9Hhq9Qk1gjrNhFQJpCy1m/5KtGszlH4ilFyBsZgTwKQiCJouF1S8RIA0PTLBF0yPtlETnA/tljSNhYogLGVIJEbSXVqW8iML60SOpVRAlwD1NNd2/8LfzrzUcjqFu5CwOzapcg2E9scmhxvKOhlQOc6Gp/y4ceSDW+JWhn9mHazAQIE8OOvfw259hAfxbrcJGfhpxxif9ryX8DFV5A0ygwkpqWDND+Sc+IzXWULeCueBKWeur5/7lgCi0rhXHFtNaKTyHV7P7PHed5vF6; WORKS_SES=eJwVULcNBEEIbAm3mJDD9F/S8xnSeKh9K2G4lVCKfIKQTEMGF3azM/SJocg7oj71EInIFI0OY00zRT+mEa5+XeuVB2DBbFh8H1QM5xR/DYYfcq4inesoo+Z0gcET/+hJdYdaH0m+AZnlDEHqtjCgKM9yE47n0vRiw4Vfp37ekAhSpwIdHL8y73+o+1fqV52ZfSM8edklte1cWxna8NSdpdsIcBoi5JlP/An5q7lUjs8i3ZqkXZ0zYz32kRpt9YF+HSmfQ1lwpEGX9W04F613rxE9GsNSXUrccqgfmwZXIg==; WORKS_USER_DOMAIN=nezumouse3; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOR2SWlX3-LRwbjH7tNc1zfCaXSPF8L8B1v7FgiQ6PRxSt4aLfiJE-Iagsp8SlT2sg-b487bZVXs-7rzJ1ObRoWwgV_60oRpscgDeKjXTabI2RY6u9UJmZmSqzYDQqLEsZw; NEO_CHK=AAAAX+gZaY2Xe4O9i5TDr145etzAjzQWSaZAZJ1Vop1RbqCgO7h6kkDsj3ax0ZtX5/g/GdoQi9zFQJFgxx3imOW7sUX7qw9PKDENoGgJjjHZeHac6PooIAHxoK6bAeA9b00EaA==; debug=false; _gid=GA1.2.2127723673.1723038301; _gat_UA-217420925-5=1; _ga_02PY6WYJV6=GS1.1.1723038301.1.0.1723038301.0.0.0; _ga=GA1.2.1549987330.1723038301; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; NNB=MLNYABTFPKZWM",
        "device-language": "ja_JP",
        "origin": "https://talk.worksmobile.com",
        "priority": "u=1, i",
        "referer": "https://talk.worksmobile.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "web-device-id": "110002509263230-349c1275-2747-5c12-edba-ce5d92a92791",
        "x-ocn": "11",
        "x-request-id": "110002509263230-349c1275-2747-5c12-edba-ce5d92a92791-1723038354702-112-origin/v4.0",
        "x-translate-lang": "ja",
    }
    payload = {"channelNo": channel_no, "serviceId": service_id}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Request failed with status code {}".format(response.status_code)}


# 使用例
channel_no = 288724441
service_id = "works"
response = get_read_infos(channel_no, service_id)
print(response)
