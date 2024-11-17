import requests

def search_channel():
    url = "https://talk.worksmobile.com/p/oneapp/client/search/searchChannel"
    params = {
        "keyword": "gwe",
        "start": 0,
        "display": 1000,
        "type": "all",
        "channelNo": "278523806",
        "msgType": "1:3:4:5:6:7:8:10:11:12:13:14:16:17:19:22:23:24:25:26:27:28:29:30:37:39:44:46:47:48:49:96:97:98",
        "timeStamp": "1718286829635"
    }
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": "language=ja_JP; LC=ja_JP; NNB=GN6PM456G5MGM; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58; debug=false; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; WORKS_USER_DOMAIN=mouse; NEO_SES=AAABIRBhrCPh429ZB+vrm9lTWaXk4Obrcg+8KHD9cr94/Lzc+63Wg8Ln38OL5QxXzhQpjG8F9kvOmiftOm0CK8XpMt/8Rrodw8qodrGzW6sEtTFsLhaWEfS2ru/QBTzPlrSe9o7T3vn1I3NcUWSDl1E1my08iVAiGkLKnOqW32mSbvZJvvOI17DQofwiUiAgFzA9fRxW/+69j6KzFw9AtPG7jef8P5j7vlBUAfEDcrS7WbZbAXkRS4wW7/56KPkSiOLqx/UN93YLELLtBZFf04KgHNlSEKY5hNSwke2MWBfGmMm7V8MGka2LTK02eL5rWTlHSm6sB2AthwiZU754r9000Orb5narDH7lYJwsYtJW81uhr7nsffd15i5EGYVRoN22goNA/q09MZHT5GN3RqRV3k0=; WORKS_SES=eJwVkLcRBEEIBFNCLcLkEPmH9LxH1QgaqH0rYbiVUIp8gpBMQwYXdrMz9ImhyDujPvUQicgUjQ5jTTNFP6cRrn5d65UnYMFsWHwfVAznFH8Nhh9yriJd6yij5nSBwRP/6El1h1qfSb4BmeUMQeq2MKAoz3ITjufS9GLDhV+nft6QCFKXAh0cP5j3H9T9K/VDZ2bfCE9edkltu9ZWhja8dGfpNgJchgh55hN/Qv5qbivHZ5FuTdKuzpmxHvtIjbb6RD9GyudQFhxp0GX13U+qDvTdAfO6d8AW81Pu/vIHo9BXpA==; NEO_CHK=AAAAYDy4picuNQCuuKBycPcnGn7UkiY7nzVLnMxIkRAhAH3Uhg5pptt6mJpImisuiIziHD1gtEsl+N0orBfW8dZzUkhAwwwXvSv7xfcRnvUWG75e9y1Mbl5KBXNlRFDl+Ape7Q==; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja"
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 呼び出し例
result = search_channel()
print(result)
