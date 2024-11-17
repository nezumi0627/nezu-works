import requests


def get_channel_members(channel_no, member_update_time=0, paging_count=500):
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/getChannelMembers"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": (
            "language=ja_JP; LC=ja_JP; NNB=HAYYJZ2FF3DWM; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; "
            "timezone=Asia/Tokyo; debug=false; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=YLg73AUFd_vD6iMx8julXzisq_bKrwo8TR6YgnvCASA; "
            'WORKS_USER_DOMAIN=sugiwaranonono; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOW1155nwmyMMjx_ctNRz_eH-EIcN5JO3YaF_zrIMaKDNiAnXDmXx2QUHzu5gZObvcjHd5xJgTtP3ULOzuoZuGAUsH1HRz5RkJZk2A2nRcFuBMb_5H15Z-ip_FzD7s1DOffTynJTTsRlrGm7PQkUJx7OX9HwllvDa5h0fxtcDOod2bHSYzROYdVOq6Xpis0E-UCrnT4Ye9TTAlP1fEahAQO06g07KHeYHApiuUKoKrErok7iaGOhR_J1BpU0gSYHQL99Ga85947xCfMY7WX4BqHHpyXMVhREENXWKw5Au91w4LZ2Em10pKKnYswaaQdIr0b52AEIGOzpvylKt9vT4lIJ076Bts8yLhct0ijygCGux3pL1PM76xGDvm3KRmQdZ7w; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; NEO_SES="AAABNRCm5x0efih8dieG71m0aFYFWcH3ZK7yWhWjQrTKh+IjAQRqJNmmqImxm6725tbPS/rs7yXnlE/TqF+VV7VJ9iekkXOL7d6NbzRi1yBaQi0z6zmd9GSmEMctQ04wlbZTdbP13+M3zqGlWKnoz34qkEmO476QABB0tuPHnJOLajORwzLuxQAxuioT9SL99ypi0xzB5k4rFAxRTKIvolmwQ5orEgIsW7cqsKktXyTuJc6SSoUOr/cLDPAw5JY73JMdKWm6+XaN0K0FsMMV+3JepC/xPIiDg3FHNdA0RKJDSI21V03WkNAPrKIH80ZSDPSplFRJTROiSCzbHQtzfy7lYakkSASog1b0uWTgnwFzK7lx6FacZF5h2XhrHM1zzAzFEbhHjSX8otYYj8jbmo4KAAxpWfYD+49I1/+0XxeoU9iy"; WORKS_SES=eJwdkccRA0EMw1pS1uqp2H9JvnEBBAdkmeGcKNjUFPrTjkyPLpW350hpWfR2oy1SBJ4+zSHUWwTntpKkOqHBmuQG/AAYtbjmwtHOseAbZuopJJTJQuzWJJjZe/Y13UWG5M2VRTR3b7ixizCc+3vI1TFO6hXbld7CRSghlqAaOptdgbmwXkob5JpfhgmmPy9L0hk0fUeldalLR/OuE5bHPlZ/okFIbiGLB3c+fC/voAJsqeaTFYLuZAq2WtfX/hlAXg1ms401Ez+0VdFjj9WCXf02836x8xwezBsN2gPY5yS5ScTpvGpuxaAC+J86aOijg3/PcCbtO/R63pzn7wfjymYn; NEO_CHK="AAAAYTZI2LmfyHuh/uezoKI2kzEqLKtuN/bxkfMcosZT6JlrR/+3cOCbIDx4V97PBDOjxj7B3MLdfTb/MU+0+whK0KqVvIBFi68vcEprS92SN5lgqahhq/8utRNsm6/kzVvIUrS83ygir3leJ8Y6M1zf94I="'
        ),
        "Device-Language": "ja_JP",
        "Origin": "https://talk.worksmobile.com",
        "Referer": "https://talk.worksmobile.com/",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Web-Device-Id": "110002509337378-7e65881d-1208-cdd5-ea53-f7251b91bb7e",
        "X-Ocn": "11",
        "X-Request-Id": "110002509337378-7e65881d-1208-cdd5-ea53-f7251b91bb7e-1724596540540-663-origin/v4.0",
        "X-Translate-Lang": "ja",
    }

    payload = {"channelNo": channel_no, "memberUpdateTime": member_update_time, "pagingCount": paging_count}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# チャンネル番号を指定してメンバー情報を取得
channel_no = 291108766
response_data = get_channel_members(channel_no)

# メンバーリストを取得
user_list = []
for member in response_data["members"]:
    user_no = member["userNo"]
    name = member.get("nickName") or member.get("i18nName") or member.get("name")
    user_list.append((user_no, name))

# 結果を表示
for user in user_list:
    print(f"userNo: {user[0]}, Name: {user[1]}")
