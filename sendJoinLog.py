import requests
import json

url = "https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage"

payload = {
    "serviceId": "works",
    "channelNo": 278523806,
    "tempMessageId": 434070220,
    "caller": {
        "domainId": 400460495,
        "userNo": 110002509004447
    },
    "extras": {
        "multilang": {
            "en": "You are using LINE WORKS, the business version of LINE. Feel free to have conversations with your exclusive business account.\n(Notifications for Events, Albums, Notes, Poll, and Live are not supported.)",
            "ja": "!!!!",
            "ko": "비즈니스 버전의 LINE, <LINE WORKS>를 사용합니다. 업무 전용 계정으로 자유롭게 대화할 수 있습니다.\n(그룹의 이벤트/앨범/노트/투표/Live 기능은 지원되지 않습니다.)",
            "zh-CN": "使用商务版LINE、<LINE WORKS>。可用业务专用账号自由聊天。\n（不支持群组活动、相册、Note、投票、Live）",
            "zh-TW": "使用業務版的LINE、<LINE WORKS>。您可以業務專用帳號自由進行對話。\n(不支援群組活動、相簿、Note、投票、Live)"
        },
        "text": "ねこねこにゃんにゃんにゃん",
        "url": "https://discord.com/invite/6bR68WcNkP"
    },
    "content": "にゃ",
    "type": 30  # 3:連絡先？小さい 4:位置情報 6:画像？ 15:?? 18:スタンプ? 19:のーと 21:小さい 22転送 トークの詳細？ 24:細長い 25:フリーズ？ 26:連絡先 29:ファイル？
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Cookie": "language=ja_JP; LC=ja_JP; NNB=GN6PM456G5MGM; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; timezone=Asia/Tokyo; TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWEcewuRP2Urig4z0bq9Wr_ajqCP1CpctsEUY6rVNy4e1DTL59xtRxpm9-1VEc9fQGSW7w-hmvMAbJJ2Bi4i_b5Eaiww_9nuWDVQ849w4ebC5eJ14BGxsmUqmI2NCu-jsSngIfqUXyBPrpxC8U7CB58; debug=false; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; WORKS_USER_DOMAIN=mouse; NEO_SES=AAABIRBhrCPh429ZB+vrm9lTWaXk4Obrcg+8KHD9cr94/Lzc+63Wg8Ln38OL5QxXzhQpjG8F9kvOmiftOm0CK8XpMt/8Rrodw8qodrGzW6sEtTFsLhaWEfS2ru/QBTzPlrSe9o7T3vn1I3NcUWSDl1E1my08iVAiGkLKnOqW32mSbvZJvvOI17DQofwiUiAgFzA9fRxW/+69j6KzFw9AtPG7jef8P5j7vlBUAfEDcrS7WbZbAXkRS4wW7/56KPkSiOLqx/UN93YLELLtBZFf04KgHNlSEKY5hNSwke2MWBfGmMm7V8MGka2LTK02eL5rWTlHSm6sB2AthwiZU754r9000Orb5narDH7lYJwsYtJW81uhr7nsffd15i5EGYVRoN22goNA/q09MZHT5GN3RqRV3k0=; WORKS_SES=eJwVkLcRBEEIBFNCLcLkEPmH9LxH1QgaqH0rYbiVUIp8gpBMQwYXdrMz9ImhyDujPvUQicgUjQ5jTTNFP6cRrn5d65UnYMFsWHwfVAznFH8Nhh9yriJd6yij5nSBwRP/6El1h1qfSb4BmeUMQeq2MKAoz3ITjufS9GLDhV+nft6QCFKXAh0cP5j3H9T9K/VDZ2bfCE9edkltu9ZWhja8dGfpNgJchgh55hN/Qv5qbivHZ5FuTdKuzpmxHvtIjbb6RD9GyudQFhxp0GX13U+qDvTdAfO6d8AW81Pu/vIHo9BXpA==; NEO_CHK=AAAAYDy4picuNQCuuKBycPcnGn7UkiY7nzVLnMxIkRAhAH3Uhg5pptt6mJpImisuiIziHD1gtEsl+N0orBfW8dZzUkhAwwwXvSv7xfcRnvUWG75e9y1Mbl5KBXNlRFDl+Ape7Q==; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja"
}

# Convert the 'extras' field to a JSON string
payload["extras"] = json.dumps(payload["extras"])

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)
