import requests


def send_image(file_path):
    # 画像ファイルの読み込み
    with open(file_path, "rb") as file:
        image_data = file.read()

    # 画像をPOSTリクエストで送信するURL
    post_url = "https://talk.worksmobile.com/p/oneapp/client/chat/issueResourcePath"

    # POSTリクエストのためのデータ
    data = {
        "serviceId": "works",
        "channelNo": 288483960,  # channelNo を整数として指定
        "filename": file_path.split("\\")[-1],  # ファイル名を抽出
        "filesize": len(image_data),
        "msgType": 11,
        "channelType": 10,
    }

    # POSTリクエストを送信する
    post_response = requests.post(
        post_url,
        json=data,
        headers={
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "Cookie": 'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; debug=false; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; _ga_02PY6WYJV6=GS1.1.1722923242.19.1.1722923315.0.0.0; _ga=GA1.2.812423193.1717075534; _ga_0PNBRDDHVC=GS1.1.1722923317.8.1.1722923323.0.0.0; NEO_CHK="AAAAX4f/gSXC1bO3RROK5l0NqlXzWuD1ijuRfH4AB/sH3y+hkLyV0XZOowdDV0EimcAee3FZp7VLoMxsc9R4D23bUijPzHooiy3AZadecMnRCamyEnq3hHi/CXQDBD62Jp4Kew=="; WORKS_SES="eJwNkMcBwEAMwlZy9/npuv9IyQAIRJnhnCjY1BT6045Mjy6Vt+dIaVn0dqMtUgSePs0h1FsE57aSpDqhwZrkBvwBGLW45sLRzrHgG2bqKSSUyULs1iSY2Xv2N91FhuTNlUU0d2+4sYswnPt7yNUxTuoV25XewkUoIZagGjqbXYG5sF5KG+Saf4YJpn8vS9IZNH1HpXWpS0fzrhOWx35W/6JBSG4hiwd3Pnwv76ACbKnmlxWC7mQKtlrX1/4bQF4NZrONNRM/tFVRSoW/wHb/BRTOdf+bQKqPbrshqm2LfLbqR8P2PoQuQ0kDvOSBV4nsRKycxqprNSCt3v0B9mpmdA==',
        },
    )

    print(post_response.json())


# 使用例
send_image("C:\\works\\icon.png")
