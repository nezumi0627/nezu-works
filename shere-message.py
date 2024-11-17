import random

import requests

url = "https://talk.worksmobile.com/gquery"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": 'language=ja_JP; LC=ja_JP; NNB=HAYYJZ2FF3DWM; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; debug=false; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJOWMPuobxwlSi7Tb7AXb03u4H7xqgHaBYNA7cfLIipu509mKBOm2lscgK_2AOXypw_0LavHOqogNkhnxAxJJgyvy7GfQyyQfLM1vCVAx2clg1Y3DD-sWdjyyI-iJ10X1ccVqa2vdrjyPQcdrAxaLXLRMT12RImoOlwPt6zVNvzjVTYL755azOiqnw-FiztR570LfYVIzWOIuJKWxyHBCjifB206LJGjZIUNBzX8Xo7kUcCoxu-PSHhrJpNo0Q1zpfTfKjpBfiwGRovpGzM4U8LdgZXG4qVRikr5zMREFVDXqTAoDaNHG674DfYjlnw_q4o_5xZuwDIZm1Y7uZpT4nMaezqe5RopDTJ3I6P_D1x517iyZqgSIR963SPT2gpnlF6V7booYKTw5USInMY10CG9arxuhdfc0J81tBkV0kQAiXKMx7V6U7dloyLnOYOYRarGhliupcMSAHD5q6waijcfA0mBgUezJnCpJdJ-K2cIdK; WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_USER_ID=DjuIDxYieNq6heFUixPuqw; WORKS_USER_DOMAIN=ncorp; NEO_SES=AAABG0hqK6XNfCClWtf8nImidtFkVxB+BoMxa7ZOIz9kE9OCqBl/qsP4BP0M2njphDW0RfI2qmdXCqfmixtpH9Bd1gImtsygEJoqrLKZvsS/lXl9rSLNyOWnXy+Kt/jTMreYqHEvm8T6arNev/LO1vljr2ACX6FV9ck4BpB/Y8TK79kdKT0udnQCA8fJzzRQKvPTHklVsQBcZPTlqtFH0qVEkoiQow13rTZutkAW/4IH/b4H7JOdYhtq78tNtHqGyKGktK//GCNsR6GNGdsmLqECjVNcmdjSPYMyjN6MOY8kgh9tf+0YPjQMOV2KWIr1nWKaNQXPqYzwh+QRyjJA3qeB+LdHkKwJcSJ87sas6a0fSo6FD6MwypYBLdRJTECd+ipDoQ==; WORKS_LOGIN_ND=Y; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja; NEO_CHK="AAAAYfYrV+jfQ7g4KDayh5iRtVo5AAafe66aegWG0839+sCvWaXqf4CQLkU1p7PVm4JcRfRoj/JGulkxxZ78JmgWg0SN5ncrSI/BdIVeDkmEFIMdz10JPp5Vvp+XV+muvD3A3HbElG/2nvIQufK260zNHC0="; WORKS_SES=eJwNz0kBwEAIBEFL3CxPTv+SEgE0U2WGc6JgU1PoTzsyPbpU3p4jpWXR2422SBF4+jSHUG8RnNtKkuqEBmuSG/APYNTimgtHO8eCb5ipp5BQJguxW5NgZu/Z/+kuMiRvriyiuXvDjV2E4dzfQ66OcVKv2K70Fi5CCbEE1dDZ7ArMhfVS2iDX/G+YYPp3WZLOoOk7Kq1LXTqad52wPPa3+ocGIbmFLB7c+fC9vIMKsKWaHysE3ckUbLWur/0XQF4NZrONNRM/tFXRKs8LSvnnVXYWL1DcVAQBIFjlrPC7CInYtPAwJL62wZ8epShbwvi389lc42sAf1dM1B/6m2Z1',
    "Device-Language": "ja_JP",
    "Origin": "https://talk.worksmobile.com",
    "Referer": "https://talk.worksmobile.com/",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Web-Device-Id": "110002509504044-587d7239-e749-a855-880e-e5f2a5b4db63",
    "X-Ocn": "11",
    # "X-Request-Id": "110002509504044-587d7239-e749-a855-880e-e5f2a5b4db63-1726979952456-638-origin/v4.0",
    "X-Translate-Lang": "ja",
}

data = {
    "operationName": "qy",
    "variables": {
        "forwardMessages": [
            {
                "tid": random.randint(1000000000, 9999999999),
                "source": {"channelNo": 296519817, "messageNo": 646},
                "target": {"channelNo": 296519335, "needSleep": False},
            },
            {
                "tid": random.randint(1000000000, 9999999999),
                "source": {"channelNo": 296519817, "messageNo": 647},
                "target": {"channelNo": 296519335, "needSleep": False},
            },
        ]
    },
    "query": """
        query qy(
            $forwardMessages: [param_forward_message!]!
        ) {
            batch_forward_message(
                forwardMessages: $forwardMessages
            ) {
                message
                result
                error
            }
        }
    """,
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
