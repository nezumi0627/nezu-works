import json

import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict(
    {
        "Cache-Control": "no-cache",
        "Content-Encoding": "gzip",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja",
        "Cookie": (
            "WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo;"
            " timezone=Asia/Tokyo; language=ja_JP; LC=ja_JP; WORKS_LOGIN_ID_LIST="
            "XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-"
            "j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q; debug=false; "
            "NNB=M4DQ4RH7SNXGM; WORKS_USER_DOMAIN=mouse; WORKS_USER_ID=ETDxRmA0AzLNTOs"
            "ITBtjxYvCq3cmJZ32C8jdyJAjcmw; NEO_SES=AAABJzWY+tTkAAoVV0ep3m8f4p0Kd7UfXu"
            "HzihzGWLZ3RSuySY7vnkoCYklrgVnm6CfVfA5aOCcDmBinQ1eMf8W5uUFqXS+dFQh8ZqlbJ"
            "gTpzaZ49alc77FyKqjsJzA/tfQ08NOZz68e1ERNs9Dm4BFY+lu6XpG9IItk98isvn1La+/qC"
            "JpzyNkcEfxgcFj3bhDIxWYuW6vuBjJVU1aqjiB6vrszik9zwO0ZgHI32JCkB6zGDqFpbBKx"
            "MYx5GBkBG17X5ek+MnKFGS0CzCeGV7pdlNwt+z5dly8xsz3O1pKGe7+kO6yo8r/quZmjqpqQ"
            "g1QuyNWpsI7gyLLa2ZCVUCjfxT9tYntcHwpEBxxWhVKdjtcwNHsupjZHactrr17QqpPlDScP0"
            "jIxeNpsDm01bhFi3hw=; NEO_CHK=AAAAYBh5gCUD5/GvJvZyhveUvlVsF9GUsaIcqMCQm/3D"
            "QPXOlsUVVfwBcwZn8blpBUTEV1UNNq9MgTDX87SnkX+RAxVZTXjO989k/frvKnhIcXf9dZA/"
            "kfhrRnbuN3Yc7EFODQ==; WORKS_SES=eJwdkMmNRUEIA1Nqdjiy5h/SfzNHJKsou1RhjuXp1"
            "BSYS0emRZew7xlgahb6brRGMj8XlxwEuYVn1FqcWMc4UJPUDz4ARC2sGlO0UeyzDVWxZGTMJ"
            "EYybWTI7D39Pt1FBufNlUY0dW+YEvvUY8KIdHzN8xq0tlkyvvi/PeaCw3029hUg1wwA9y3DR2"
            "aO2/40MO27MuaRB7Tyrh5rHqjOiDuRFADwbYJfis8rla/ufDzR++PW+DfWzGmVNWYHGuG7QEp"
            "PBUcaYYzFo4wGmU/bWH26qxLxKdCRtxt/O0ZBj0yK8Kw69POFz/pq94GYP3pem6gHye1x16b"
            "Muifw5d8PO6NlWg=="
        ),
        "Device-Language": "ja_JP",
        "Origin": "https://talk.worksmobile.com",
        "Referer": "https://talk.worksmobile.com/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
        "like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Web-Device-Id": "110002509004447-06d80975-c25c-11f0-5911-9d43207176bc",
        "X-Ocn": "11",
        "X-Request-Id": "110002509004447-06d80975-c25c-11f0-5911-9d43207176bc-1721365768671-861-"
        "origin/v4.0",
        "X-Translate-Lang": "ja",
    }
)

payload = {
    "serviceId": "works",
    "channelNo": 278287860,
    "userNo": 110002509004447,
    "fromMessageNo": 6424,
    "toMessageNo": 6443,
}

url = "https://talk.worksmobile.com/p/oneapp/client/chat/getMessageListByRange"
response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
print(response.json())
