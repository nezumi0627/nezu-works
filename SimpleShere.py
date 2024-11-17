import random

import requests


def gquery_request(source_channel_no, source_message_no, target_channel_no):
    """
    This function sends a POST request to the Worksmobile API
    and returns the response as a JSON object.

    Args:
        source_channel_no (int): The channel number of the source message.
        source_message_no (int): The message number of the source message.
        target_channel_no (int): The channel number of the target message.

    Returns:
        dict: The response from the Worksmobile API as a JSON object.

    Raises:
        Exception: If the request fails or returns an error status code.
    """
    url = "https://talk.worksmobile.com/gquery"

    # Define the headers for the request
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "content-length": "545",
        "content-type": "application/json;charset=UTF-8",
        "cookie": (
            "language=ja_JP; LC=ja_JP; _mkto_trk=id:227-YJI-053&token:"
            "_mch-worksmobile.com-1717075533491-42520; NNB=MVJDTEKMPZMGM;"
            "_gcl_au=1.1.357572222.1717075534; _yjsu_yjad=1717075534."
            "62eb9907-1ad4-4d4d-b028-c2157639e4d6; timezone=Asia/Tokyo;"
            "TZ=Asia/Tokyo; WORKS_LOGIN_TYPE=id; WORKS_RE_LOC=jp1; "
            "WORKS_TE_LOC=jp1; WORKS_USER_ID=mnrx7ZmJfKlr5le5QNesD1u-Cpb4fu"
            "18m_n2LQU-b88; WORKS_USER_DOMAIN=nezumouse3; _uetvid=1895b0d0"
            "1e8811efa4551b9a59d68d81; _ga_LG7FMZLY53=GS1.1.1722490553.8."
            "1.1722490671.15.0.0; _gid=GA1.2.1423597533.1722766902; _ga_BV"
            "5Q99B5L5=GS1.1.1722785396.2.1.1722786107.0.0.0; _ga_49XKN1QV2T"
            "=GS1.1.1722786154.1.1.1722786552.0.0.0; _ga_KY0FKGPQV9=GS1.1.1"
            "722791197.1.0.1722791197.0.0.0; _ga_03NNQM7KD0=GS1.1.172288353"
            "4.8.1.1722883578.0.0.0; _ga_0HE1S6EWD5=GS1.1.1722883627.2.0."
            "1722883631.0.0.0; _ga_E1JVY76ZGR=GS1.2.1722883637.1.1.1722883"
            "637.0.0.0; _ga_BLYDRQHTGP=GS1.1.1722883636.1.1.1722883638.0.0"
            ".0; debug=false; org.springframework.web.servlet.i18n.CookieLoca"
            "leResolver.LOCALE=ja; _ga=GA1.2.812423193.1717075534; NEO_CHK="
            '"AAAAYMU/z3dEQZpnG7kvDQhLKis3I6KLL4eVDvP07/oO9c33WKpx5tUDJI9DLW'
            "9RskJF1/MnVhtXpsTnVdD+MT52hPp/qjUj4G9Cy3eNSI1qwBs2viR2bV0pGermBG"
            'd+wssBaw=="; NEO_SES="AAABJdTsezqZcwUrjKJJnBia/g6Qwd2IyaNv6D5K1U'
            "FnI3Tb4nDoaYZX295dmh8VQjeTqefXoyvb4yGmpPppZeeMhX5LFBi6oCSe0J/Reh"
            "3GTjZVDjjQ09E1gX+iH02Mwpt2/+m52rUKcCIWHGZ16/4jaCLgCmVgnPPlBaTS7J"
            "8IZts96+pIucWvbORPxn+07TaO61l2+/7vfWm7fAPgUUwEThSH3KPqCR4ggh7bcJx"
            "ZFz8gp76NihN4MZtLfGok/JtKJ4ADqtMzfDql3doBYiZJ24J0Xqs2Wi3TD9a9PXxR"
            "FjucWIT54wgk/glO0R87jbIic6NbIUKOSGR21n34Rh7ioubvmQnqxXK2tMa6LB3Jt"
            'lMPga1df+3RWUHwxzfSbzQx8ZJg2rLd7b4uCUy+kRUMT40="; WORKS_SES=eJ'
            "wNkLkBwEAIw1biJ5S8+4+UKylsS5QZzomCTU2hf9qR6dGl8u05UloWfbvRFikCn36"
            "aQ6i3CM5tJUl1QoM1yQ34CjBqcc2Fo51jwTfM1FNIKJOF2K1JMLP37C3dRYbkzZVF"
            "NHdvuLGLMJz79yFXxzipV2xXegsXoYRYgmrobHYF5sJ6KW2Qa74ME0w/L0vSGTT9"
            "jkrrUpeO5rtOWB57Xf1Eg5DcQhYP7nz4vryDCrClmicrBN3JFGy1rl/7M4C8GsxmG2"
            "sm/tBWRSkV3oDtPgIK57r3TSDVj267rT3eFen2vfIzfKbREJxV8uhDi4gYZMIfh7h"
            'pdou3mejeD+ymZmw="'
        ),
        "device-language": "ja_JP",
        "origin": "https://talk.worksmobile.com",
        "priority": "u=1, i",
        "referer": "https://talk.worksmobile.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        ),
        "web-device-id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c",
        "x-ocn": "11",
        # "x-request-id": "110002509263230-586b2cc7-93ef-94a0-32a0-48015bc4938c-1722919904791-376-origin/v4.0",
        "x-translate-lang": "ja",
    }

    data = {
        "operationName": "qy",
        "variables": {
            "forwardMessages": [
                {
                    "tid": random.randint(1000000000, 9999999999),
                    "source": {
                        "channelNo": source_channel_no,
                        "messageNo": source_message_no,
                    },
                    "target": {"channelNo": target_channel_no, "needSleep": False},
                }
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

    return response.json()


# example
result = gquery_request(288525027, 21, 287933058)  # channelNo(source) messageNo channelNo(target)
print(result)
