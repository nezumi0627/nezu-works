import json
import urllib.parse

import requests

# デコードされたペイロードをここに設定
decoded_payload = {
    "serviceId": "works",
    "channelNo": 288320617,
    "tempMessageId": 921413340,
    "caller": {"domainId": 400486244, "userNo": 110002509263230},
    "extras": "",
    "content": '<m userNo="913000043047576">@ねずみ</m>',
    # "msgTid": 921413340,
    "type": 10,
}

# ペイロードをエンコードして送信する
encoded_payload = urllib.parse.urlencode({"payload": json.dumps(decoded_payload)})

url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"
headers = {
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Origin": "https://talk.worksmobile.com",
    "Referer": "https://talk.worksmobile.com/",
    "Cookie": 'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; debug=false; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_0PNBRDDHVC=GS1.1.1722791198.6.1.1722791279.0.0.0; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; _ga_0HE1S6EWD5=GS1.1.1722791295.1.0.1722791296.0.0.0; _ga=GA1.1.812423193.1717075534; _ga_03NNQM7KD0=GS1.1.1722790587.7.1.1722791504.0.0.0; _ga_02PY6WYJV6=GS1.1.1722786666.12.1.1722791590.0.0.0; NEO_CHK="AAAAYYj8jzAEYw5/pNAkraIlyKEGL/FaQ3h4i1Fa3ji7m2RaEl6jvoR8Vl9SjQJEJV8KQg07RtnAIKUNSWx9KqP/uZ80fPSbFknvsNZmBPiR9/Dqb4KHe9l4VtXNsjvIqTsGgXDWmBPxYvEAf4yD+ON7c70="; WORKS_SES=eJwNkckRAFEEBVOyG0dr/iHNPyrltabMcE4UbGoK/dOOTI8ulW/PkdKy6NuNtkgR+PTTHEK9RXBuK0mqExqsSW7AF4BRi2suHO0cC75hpp5CQpksxG5Ngpm9Z490FxmSN1cW0dy94cYuwnDu34dcHeOkXrFd6S1chBJiCaqhs9kVmAvrpbRBrvlmmGD6eVmSzqDpd1Ral7p0NN91wvLYy+onGoTkFrJ4cOfD9+UdVIAt1TxZIehOpmCrdf3anwHk1WA221gz8Ye2Kkqp8AC2+zagcK571wRS/ei2mx6mp2ornsaMA4n6aNVry8n6JgPMvioY44v3DfqogT5n7x8B0mas',
}

response = requests.post(url, headers=headers, data=encoded_payload)
print(response.status_code)
print(response.json())
