import json

import requests

url = "https://talk.worksmobile.com/p/oneapp/client/chat/ackMessage"
headers = {
    "authority": "talk.worksmobile.com",
    "method": "POST",
    "path": "/p/oneapp/client/chat/ackMessage",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "content-type": "application/json;charset=UTF-8",
    "cookie": (
        'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; _ga_0PNBRDDHVC=GS1.1.1722397510.5.1.1722397802.0.0.0; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _ga_03NNQM7KD0=GS1.1.1722490672.6.1.1722490704.0.0.0; debug=false; _gid=GA1.2.1423597533.1722766902; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; _ga_02PY6WYJV6=GS1.1.1722773080.11.1.1722775866.0.0.0; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga=GA1.1.812423193.1717075534; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786179.0.0.0; NEO_CHK="AAAAYQohVTSH3FG7vHrhm1ef17D0PHX6u0Pol+QJsGjFRk4uEe83HgDAOnwCrLI6P6zvA9TS787OBgzoTCgIl8QQtDwM/DWkajK5uK5VYJkCE9TOTViwt55VEumypYRnOkC/tZjSnQdiJI34/zIjQ0m40SE="; WORKS_SES=eJwNkMcBwEAIw1aiczyp+4+U/I2FXGY4Jwo2NYX+tCPTo0vl7TlSWha93WiLFIGnT3MI9RbBua0kqU5osCa5Af8CjFpcc+Fo51jwDTP1FBLKZCF2axLM7D37SXeRIXlzZRHN3Rtu7CIM5/4ecnWMk3rFdqW3cBFKiCWohs5mV2AurJfSBrnmf8ME07+XJekMmr6j0rrUpaN51wnLY39X/6JBSG4hiwd3Pnwv76ACbKnmlxWC7mQKtlrX1/4bQF4NZrONNRM/tFVRSoUfYLv/BxTOdf+aQKqPbrt1ivgPPvj9Qln1t2Kl5/34bEhq+PmK4Du0BnGg+rk7/vP2A+PHZkA=; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja'
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
    "web-device-id": "110002509263230-9bc65e71-3e5c-b10c-e426-bd0f735beafd",
    "x-ocn": "11",
    # "x-request-id": "110002509263230-9bc65e71-3e5c-b10c-e426-bd0f735beafd-1722786502270-437-origin/v4.0",
    "x-translate-lang": "ja",
}

data = {
    "serviceId": "works",
    "messageNo": 200,
    "userNo": 110002509263231,
    "channelNo": 288965904,
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
