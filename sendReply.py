import json

import requests

url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Origin": "https://talk.worksmobile.com",
    "Referer": "https://talk.worksmobile.com/",
    "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Ocn": "11",
    "X-Request-Id": "110002509263230-978aa147-c078-caa9-562b-80a8c3aeee3c-1722767065571-177-origin/v4.0",
    "X-Translate-Lang": "ja",
    "Web-Device-Id": "110002509263230-978aa147-c078-caa9-562b-80a8c3aeee3c",
}

cookies = {
    "language": "ja_JP",
    "LC": "ja_JP",
    "_mkto_trk": "id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520",
    "NNB": "MVJDTEKMPZMGM",
    "_gcl_au": "1.1.357572222.1717075534",
    "_yjsu_yjad": "1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6",
    "timezone": "Asia/Tokyo",
    "TZ": "Asia/Tokyo",
    "_ga_0PNBRDDHVC": "GS1.1.1722397510.5.1.1722397802.0.0.0",
    "WORKS_LOGIN_TYPE": "id",
    "WORKS_RE_LOC": "jp1",
    "WORKS_TE_LOC": "jp1",
    "WORKS_USER_ID": "mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88",
    "WORKS_USER_DOMAIN": "nezumouse3",
    "_uetvid": "1895b0d01e8811efa4551b9a59d68d81",
    "_ga_LG7FMZLY53": "GS1.1.1722490553.8.1.1722490671.15.0.0",
    "_ga_03NNQM7KD0": "GS1.1.1722490672.6.1.1722490704.0.0.0",
    "debug": "false",
    "NEO_SES": "AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40=",
    "WORKS_SES": "eJwVjscRADEIA1simfDEhP5LOt+PGe0KUftWwnAroRT5BCGZhgwu7GZn6BFDkfNAPeohEpEpGh3GmmaK/kgjXL1d65UvwILZsLgXKoZzim+D4UXOVaTXOsqoOV1gcMQvHanuUOsHyR2QWc4QpG4LA4ryLDfhOC5NJzZc+HTq9YZEkHoW6OD4G3P+Q91vqb/pzOwb4cnLLqltr7WVoQ2f3Vm6jQDPIUKeueJHyE/N+8pxLdKtSdrVOTPWYw+p0Va/0N9GyuNQFhxp0GXedXUqmTXw9uye23G3Tt9K6g+j7Fe9",
    "NEO_CHK": "AAAAYANIbtebVvg1cYep+2NjJnL+dlNMlL5w26Z0qzT5w38BvRNIBrMQfQi+6iNkUQYy+zLzDHlkaYCpCnk/l1cIbwVNK9HknFz8t5avVzzBudLUMY7zVHSD1HnSBa6ptvJ7aQ==",
    "_gid": "GA1.2.1423597533.1722766902",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
    "_gat_UA-69563150-12": "1",
    "_ga": "GA1.1.812423193.1717075534",
    "_ga_BV5Q99B5L5": "GS1.1.1722767009.1.0.1722767013.0.0.0",
    "_ga_02PY6WYJV6": "GS1.1.1722766896.10.1.1722767055.0.0.0",
}

payload = {
    "serviceId": "works",
    "channelNo": 287929261,
    "tempMessageId": 670653960,
    "caller": {"domainId": 400486244, "userNo": 110002509263230},
    "extras": '{"referenceMessageInfo":{"messageNo":2}}',
    "content": "@",
    # "msgTid": 670653960,
    "type": 37,
}

response = requests.post(
    url, headers=headers, cookies=cookies, data=json.dumps(payload)
)

print(response.status_code)
print(response.json())
