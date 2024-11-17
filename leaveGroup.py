import requests

cookies = {
    'language': 'ja_JP',
    'LC': 'ja_JP',
    'NNB': 'GN6PM456G5MGM',
    'WORKS_RE_LOC': 'jp1',
    'WORKS_TE_LOC': 'jp1',
    'timezone': 'Asia/Tokyo',
    'TZ': 'Asia/Tokyo',
    'WORKS_LOGIN_TYPE': 'id',
    'WORKS_USER_DOMAIN': 'agroupofmice',
    'WORKS_USER_ID': 'LWxTHdDaKJ7MW-Edx8ADH66cCwHqJpX8m3zY-2dmW7o',
    'NEO_SES': 'AAABJYbong3sQfy23Bzgm3tmECLdNqLSVVNnXdHO0itAMNY+/NJQLQTMMy6X5X+C17ICct4VI3ZeQYwJ9flEiGT4V4BOgBVdaZ1jTkltwjga/olAOELvG/nzIgH4eO76iXe4y5DyCZfblXX/v60t/HCIP41nYLB01WrVcqW6P84qUyR0J0Sg3IC8UsKqppi2WEUr1wDMio0pI5R0/lQD4GSKM+DxtTPep/dMfdCaVlcZwyZvVB9xXKpX5DE436j3+lOdsCrds2M5ZXCnBGq0g0ACBKl5PZX3pgXcJhuRfH0wWaQhT8q0Wv3s5rBKcUTzB022GY4yfWBGew70vk/xztF+V/JXdzL3ywosqe752zxX+V6mk9b046vz9X0SKhNY4uiJFI5cX1czEvsJRrN3mZmODHI=',
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Request-Id": "110002508880628-00abf68c-38f7-1d98-88e5-f47a8dc68d9d-1717071649580-418-origin/v4.0",
}

payload = {
    "channelNo": 0,
    "channelNoList": [276130319]
}

response = requests.post('https://talk.worksmobile.com/p/oneapp/client/chat/quit', headers=headers, cookies=cookies, json=payload)

print(response.text)
