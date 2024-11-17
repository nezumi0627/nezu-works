import requests

def get_channel_info(channel_no):
    url = "https://talk.worksmobile.com/p/oneapp/client/chat/getChannelInfo"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": "language=ja_JP; LC=ja_JP; NNB=GN6PM456G5MGM; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58; debug=false; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; WORKS_USER_DOMAIN=mouse; NEO_SES=AAABIRBhrCPh429ZB+vrm9lTWaXk4Obrcg+8KHD9cr94/Lzc+63Wg8Ln38OL5QxXzhQpjG8F9kvOmiftOm0CK8XpMt/8Rrodw8qodrGzW6sEtTFsLhaWEfS2ru/QBTzPlrSe9o7T3vn1I3NcUWSDl1E1my08iVAiGkLKnOqW32mSbvZJvvOI17DQofwiUiAgFzA9fRxW/+69j6KzFw9AtPG7jef8P5j7vlBUAfEDcrS7WbZbAXkRS4wW7/56KPkSiOLqx/UN93YLELLtBZFf04KgHNlSEKY5hNSwke2MWBfGmMm7V8MGka2LTK02eL5rWTlHSm6sB2AthwiZU754r9000Orb5narDH7lYJwsYtJW81uhr7nsffd15i5EGYVRoN22goNA/q09MZHT5GN3RqRV3k0=; WORKS_SES=eJwVkLcRBEEIBFNCLcLkEPmH9LxH1QgaqH0rYbiVUIp8gpBMQwYXdrMz9ImhyDujPvUQicgUjQ5jTTNFP6cRrn5d65UnYMFsWHwfVAznFH8Nhh9yriJd6yij5nSBwRP/6El1h1qfSb4BmeUMQeq2MKAoz3ITjufS9GLDhV+nft6QCFKXAh0cP5j3H9T9K/VDZ2bfCE9edkltu9ZWhja8dGfpNgJchgh55hN/Qv5qbivHZ5FuTdKuzpmxHvtIjbb6RD9GyudQFhxp0GX13U+qDvTdAfO6d8AW81Pu/vIHo9BXpA==; NEO_CHK=AAAAYDy4picuNQCuuKBycPcnGn7UkiY7nzVLnMxIkRAhAH3Uhg5pptt6mJpImisuiIziHD1gtEsl+N0orBfW8dZzUkhAwwwXvSv7xfcRnvUWG75e9y1Mbl5KBXNlRFDl+Ape7Q==; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja"
    }

    payload = {
        "channelNo": str(channel_no),
        "direction": "0",
        "messageNo": "0",
        "recentMessageCount": "0"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        channel_info = response_data.get("channelInfo", {})
        return channel_info
    else:
        print("エラーが発生しました:", response.status_code)
        return None

# 使用例
channel_info = get_channel_info(278290853)
if channel_info is not None:
    print("Channel No:", channel_info.get("channelNo"))
    print("Channel Type:", channel_info.get("channelType"))
    print("User Count:", channel_info.get("userCount"))
    print("Title:", channel_info.get("title"))
    print("Photo Path:", channel_info.get("photoPath"))
else:
    print("チャンネル情報を取得できませんでした。")
