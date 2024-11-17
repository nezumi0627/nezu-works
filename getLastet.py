import requests


def fetch_and_print_messages():
    # 設定
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/getContentMessageListByRange"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Cookie": 'language=ja_JP; LC=ja_JP; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; WORKS_USER_DOMAIN=nezumouse3; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu18m_n2LQU-b88; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOR2SWlX3-LRwbjH7tNc1zfCaXSPF8L8B1v7FgiQ6PRxSt4aLfiJE-Iagsp8SlT2sg-b487bZVXs-7rzJ1ObRoWwgV_60oRpscgDeKjXTabI2RY6u9UJmZmSqzYDQqLEsZw; _gid=GA1.2.2127723673.1723038301; NNB=MLNYABTFPKZWM; NEO_SES="AAABMTpiM9SrmYd67xKCptJnYY0Ek2DDnVjVVWwFiFLqx7N3EHgkgS9rs+M2Ee8cVd3tn+o0LoLd/+HdkqjsVNuRipYeriSbFOrUjPMY48iO9trfJ9Kb75Evs3HkYFR5lq3bxoU+bcdu9bT74UbBCAR57QokfZF9Hhq9Qk1gjrNhFQJpCy1m/5KtGszlH4ilFyBsZgTwKQiCJouF1S8RIA0PTLBF0yPtlETnA/tljSNhYogLGVIJEbSXVqW8iML60SOpVRAlwD1NNd2/8LfzrzUcjqFu5CwOzapcg2E9scmhxvKOhlQOc6Gp/y4ceSDW+JWhn9mHazAQIE8OOvfw259hAfxbrcJGfhpxxif9ryX8DFV5A0ygwkpqWDND+Sc+IzXWULeCueBKWeur5/7lgCi0rhXHFtNaKTyHV7P7PHed5vF6"; _ga_03NNQM7KD0=GS1.1.1723041541.1.0.1723041543.0.0.0; debug=false; NEO_CHK="AAAAYTNF+71hIKb+yaMi7BiIhHflZv+oJZI8CGBh86ORK8jhFRNltVyo8Zkq/FzG3uWbVTk3Kb+x/OkonVvnvuVVk5i/UGd/Y7ZpNr6Qx0HbOsKs5kxkJmV+hQQoVjR3pJe/r9iosTTBNN8FVyqjuGa2kQE="; WORKS_SES=eJwVkckBA0EIw1riZnly9l9SJn+wkSgznBMFm5pC/7Qj06NL5dtzpLQs+najLVIEPv00h1BvEZzbSpLqhAZrkhvwBWDU4poLRzvHgm+YqaeQUCYLsVuTYGbv2Wu6iwzJmyuLaO7ecGMXYTj370OujnFSr9iu9BYuQgmxBNXQ2ewKzIX1Utog13w7TDD9uCxJZ9D0OyqtS106mu86YXnsZfUDDUJyC1k8uPPh+/IOKsCWah6sEHQnU7DVun7tjwDyajCbbayZ+ENbFaVUeAW2+y6gcK57NoFUP7rtHsf5+/dwfRqyWzDW8TtTS5fdsvqsXwhpEmmBPBdvEvm9IX7362aH; _ga=GA1.1.1549987330.1723038301; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; _ga_02PY6WYJV6=GS1.1.1723125908.8.1.1723128972.0.0.0',
        "X-Requested-With": "XMLHttpRequest",
    }
    payload = {
        "rangeFlag": 1,
        "baseMessageNo": 776,
        "startTime": 0,
        "channelNo": 288724441,
        "limit": 100,
        "contentType": 1,
    }

    # リクエストの送信
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # HTTP エラーが発生した場合に例外を発生させる

        # レスポンスの JSON データを取得
        data = response.json()
        print("Response JSON Data:")
        print(data)  # レスポンスの内容を出力

        # "beforeMessageList" から messageNo を取得して、若い順に並べる
        messages = data.get("result", {}).get("beforeMessageList", [])
        sorted_messages = sorted(messages, key=lambda msg: msg.get("messageNo", float("inf")))

        # messageNo を出力
        for msg in sorted_messages:
            print(f"MessageNo: {msg.get('messageNo')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# 使用例
fetch_and_print_messages()
