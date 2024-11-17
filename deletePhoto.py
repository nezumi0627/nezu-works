import requests


def deletePhoto():
    url = "https://admin.worksmobile.com/api/Z846869/contact/adminapi/v1/users/110002509263230/photo"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Content-Length": "2",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": 'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; NEO_CHK="AAAAYTciuDfUR8rptTl0gm7fZltshofuNuLs2ZPyZQhBvUX3OYZRo2jYwJ0UvMgnIMw+4/f6tLUNY9C4kKhegpIiEBwYjH2gMa9FxUCbjIJc2tDLg4qWh0ADy9OsdoIiL1LrbROWHtZvlP5JXPpUWeuuhzI="; WORKS_SES=eJwVkEcBA0EMxCi5+/x05Q8pGwBTpDLDOVGwqSn0TzsyPbpUvj1HSsuibzfaIkXg009zCPUWwbmtJKlOaLAmuQFfAUYtrrlwtHMs+IaZegoJZbIQuzUJZvaevaW7yJC8ubKI5u4NN3YRhnP/PuTqGCf1iu1Kb+EilBBLUA2dza7AXFgvpQ1yzZdhgunHZUk6g6bfUWld6tLRfNcJy2Ovqx9oEJJbyOLBnQ/fl3dQAbZU82CFoDuZgq3W9Wt/BJBXg9lsY83EH9qqKKXCG7Dd94DCue7ZBFL96Lb7ebpwx1n4g24g3WS9kzpaKavs+5C/y7fRkkZZ31MrbAjaP/p9Zog=; _ga_02PY6WYJV6=GS1.1.1722923242.19.1.1722923315.0.0.0; _gat_UA-110924794-12=1; SHOW_INQUIRY_TOOLTIP=Y; _ga=GA1.2.812423193.1717075534; _ga_0PNBRDDHVC=GS1.1.1722923317.8.1.1722923323.0.0.0; NEO_CHK="AAAAYMOXEBVxVAf7f3ZFRwYp7ekTsLEc5dHfT0oRUExIvjjKVhAqbSKGYWGXFOcn9wcC7LWC9sicghR1sAtFs54K7jkcjv94mlEjQtb8Mc8BZ0tL1j05HqagCwc18u3NgRA5fg=="; WORKS_SES=eJwV0McBA0EIA8CWyBxPYv8leV0AQqMywzlRsKkp9E87Mj26VL49R0rLom832iJF4NNPcwj1FsG5rSSpTmiwJrkBXwBGLa65cLRzLPiGmXoKCWWyELs1CWb2nr1Pd5EheXNlEc3dG27sIgzn/n3I1TFO6hXbld7CRSghlqAaOptdgbmwXkob5Jrvhgmmn8uSdAZNv6PSutSlo/muE5bHXlY/aBCSW8jiwZ0P35d3UAG2VPOwQtCdTMFW6/q1PwHk1WA221gz8Ye2Kkqp8B7Y7mtA4Vz31gRS/ei2++104Y6z8IduIN1kvZI6Win6dDuTEW9ug/tg/rCo5tul+AH+AGbe',
        "Origin": "https://admin.worksmobile.com",
        "Priority": "u=1, i",
        "Referer": "https://admin.worksmobile.com/member/users",
        "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }

    try:
        # DELETEリクエストを送信
        response = requests.delete(url, headers=headers, data={})

        # レスポンスのステータスコードを確認
        if response.status_code == 204:
            print("Photo deleted successfully.")
        else:
            print(f"Failed to delete photo. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")


# 関数を呼び出す
deletePhoto()
