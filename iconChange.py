import requests


def upload_icon(file_path, api_url):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "Referer": "https://admin.worksmobile.com/member/users",
        "Origin": "https://admin.worksmobile.com",
        "Cookie": 'language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM; _gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534.62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d01e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8.1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.1722883534.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0.1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0.0; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1UFnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJxZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxRFjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3JtlMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; _ga_02PY6WYJV6=GS1.1.1722923242.19.1.1722923315.0.0.0; SHOW_INQUIRY_TOOLTIP=Y; _ga=GA1.2.812423193.1717075534; _ga_0PNBRDDHVC=GS1.1.1722923317.8.1.1722923323.0.0.0; NEO_CHK="AAAAYf7tKQkB9pK4+hHJV7A5gUdqkS85bDEOsefA9i9nej4jBEriC1WLvv178OGDDUJCrVgDc1Dz6tLfZAJ8tCDCNMTn/4zdOPua15X/Bd/s64HD6LRzyqEZHH8aiNb3LbmBIYaNIIpnZZw1yIS7uVsjW5U="; WORKS_SES=eJwNkbkBAEEIAlvy9wx9+y/pNjMRGCgznBMFm5pC/7Qj06NL5dtzpLQs+najLVIEPv00h1BvEZzbSpLqhAZrkhvwCWDU4poLRzvHgm+YqaeQUCYLsVuTYGbv2XO6iwzJmyuLaO7ecGMXYTj370OujnFSr9iu9BYuQgmxBNXQ2ewKzIX1Utog13w/TDD9uCxJZ9D0OyqtS106mu86YXnsafUDDUJyC1k8uPPh+/IOKsCWah6sEHQnU7DVun7tjwDyajCbbayZ+ENbFaVUeAa2+xJQONe9NoFUP7rthqi2LfLZqicN2/shdBlKGqCgvTv23gCvYTt0rwGjdMoX/gf6OmaZ',
    }

    try:
        with open(file_path, "rb") as file:
            response = requests.post(
                api_url,
                files={"file": ("icon.png", file, "image/png")},
                headers=headers,
            )

        response.raise_for_status()  # HTTPエラーを発生させる

        # 成功した場合の処理
        print("アイコンのアップロードに成功しました。")
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # エラー詳細を表示
        print(f"リクエスト中にエラーが発生しました: {e}")
        if response is not None:
            print(f"サーバーからのレスポンス: {response.text}")
        return None


# 使用例
file_path = "C:\\works\\icon.png"  # 実際のファイルパスに置き換えてください
api_url = "https://admin.worksmobile.com/api/Z846869/contact/adminapi/v1/users/110002509263230/photo"
upload_icon(file_path, api_url)
