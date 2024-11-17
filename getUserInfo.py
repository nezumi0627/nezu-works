import requests
import json
getChannelMembers = "https://talk.worksmobile.com/p/oneapp/client/chat/getChannelMembers"
getUserInfoBase = "https://talk.worksmobile.com/p/contact/v4/users/"
payload = {
    "channelNo": 278523806,
    "memberUpdateTime": 0,
    "pagingCount": 500
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "language=ja_JP; LC=ja_JP; NNB=GN6PM456G5MGM; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58; debug=false; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; WORKS_USER_DOMAIN=mouse; NEO_SES=AAABHssbyZce+YIyJ0X+WONrn2SfeEwXY7EfKUxoP1FyhqFiIxtu+E0rPPyM+W73y46gERQ85kVXoxVijsR4ZfWutApNd+3LuKfCj3oG/9DQjbKBkdX86k5XQwQ26Q1U2rY+Vv2zppBai6xk4hacukAw01P2pI/WEIvjjmn+mEM1Gi1tdGDLytk+iqqwG/bVdzZi4pxw8eT7MDSyykm3oZBNKfeD5ktxJJOMqH03sCJldojDBIY69ral1wuJrdm4C3yCaMRlYXXevTfKJGNQb17qbjnPG/uyB6AuMgpsJDpJZ1fmp6+3AUiXQovUoYGiBhWMaAcwkXG0zcfpS5frIFa4ZlyScFhEvcMS6GK5k/7+yFjuYC6j7rh0tC1iz9A/xxFfDQ==; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; NEO_CHK=AAAAYWQyCkYzPxiapoXHY02rB23hvB2yqBZee1e+Uozo3Tu1S0PjWlDVwqvqZIW7qCZCJL3lqJthZjW0yBK1K2p2bRO0AGwlMzkWcjOZjn6ky79LJgToQb8nm3ClSbE9fY8HVT3fZB6VV9ttDObHbHQ5VHI=; WORKS_SES=eJwNkbkNwEAMw1by73Ppd/+RkloQBUJlhnOiYFNT6E87Mj26VN6eI6Vl0duNtkgRePo0h1BvEZzbSpLqhAZrkhvwB2DU4poLRzvHgm+YqaeQUCYLsVuTYGbv2b90FxmSN1cW0dy94cYuwnDu7yFXxzipV2xXegsXoYRYgmrobHYF5sJ6KW2Qa/4dJpj+vSxJZ9D0HZXWpS4dzbtOWB77Wf2LBiG5hSwe3PnwvbyDCrClml9WCLqTKdhqXV/7bwB5NZjNNtZM/NBWRWOd+ffzOGx+rJV4LFuChz90Zf4YaCZTr/EVLZIYvoP3P5IDCrLxSBsexEun+R/ZSEMm/wDnEGY7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

params = {"domainId": 0, "client": "PC_WEB"}

response = requests.post(getChannelMembers, headers=headers, json=payload)

if response.status_code == 200:
    print("チャンネルメンバーの取得に成功しました！")
    data = response.json()
    members = data.get("members", [])
    member_nos = [member['userNo'] for member in members]

    # 各ユーザーの情報を取得
    for member_no in member_nos:
        getUserInfo = getUserInfoBase + str(member_no)
        user_response = requests.get(getUserInfo, headers=headers, params=params)
        if user_response.status_code == 200:
            user_info = user_response.json()
            with open(f"./members/user_{member_no}.json", "w", encoding="utf-8") as f:
                json.dump(user_info, f, ensure_ascii=False, indent=4)
        else:
            print(f"ユーザー情報の取得に失敗しました: {member_no}")
else:
    print("チャンネルメンバーの取得に失敗しました！")
    print(response.status_code)
    print(response.text)

