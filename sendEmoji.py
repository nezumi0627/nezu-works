import requests
import json

payload = {
    "serviceId": "works",
    "channelNo": 278287860,
    "tempMessageId": 128496670,
    "caller": {
        "domainId": 400460495,
        "userNo": 110002509004447
    },
    "content": "<e class=\"/3/1.1/100178\">(love)</e>",
    "extras": {},  # 空の辞書として設定する
    "type": 27
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Cookie": "WORKS_LOGIN_TYPE=id;TZ=Asia/Tokyo;timezone=Asia/Tokyo;WORKS_TE_LOC=jp1;language=ja_JP;WORKS_RE_LOC=jp1;NEO_SES=AAABHrDtaM/juLbmGorHaZiZeyIUWCFXz546QMoouc5sjEVjpoDabj+Ox2gOJ+6FE2p5p3VJiGb8P27XDr+sYcKqUmXzj5zIC8U0buQuKcKE6Y2TQnxbcOqL7nCNHSzCltEYkwFf/mVFQ9uJgr0pIa+CUSq+TJiS2lh6LxMR78tJhcrM/v07Mz9RK88Gp07c2YAXCFeYdANeVf5zCbTg8c+8YwSZn0Z6QWDO+j5TChcInD3O5PFucSUEdq3WWZXxvvpl+xyn0rMe/o/pcUAAi6TWdT6HEsg2yoA5RmkquXJXAKb0w8Wku0HobQaV22jsvmiBKp4u4qbJYJJ9RrcUq6c/r5mbVuMhzG32zjXOxo14DcjQZ5Il3rhM8ssTUJnD6+egqg==;WORKS_SES=eJwVULcRBEEIawm3mJDD9F/S8xkzMkii9q2E4VZCKfIJQjINGVzYzc7QJ4Yi74j61EMkIlM0Oow1zRT9mEa4+nWtVx6ABbNh8X1QMZxT/DUYfsi5inSuo4ya0wUGT/yjJ9Udan0k+QZkljMEqdvCgKI8y004nkvTiw0Xfp36eUMiSJ0KdHD8wrz/oe5fqV90ZvaN8ORll9S2c21laMNTd5ZuI8BpiJBnPvEn5K/mvnJ8FunWJO3qnBnrsY/UaKsP9MtI+RzKgiMNugzYJvUKJ1wx+e8103Zz+z8r/wCdA1dT;WORKS_USER_DOMAIN=mouse;WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw;LC=ja_JP;WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q"
}
# extrasをJSON文字列に変換する
payload["extras"] = json.dumps(payload["extras"])

# リクエストの送信
try:
    response = requests.post('https://talk.worksmobile.com/p/oneapp/client/chat/sendMessage', headers=headers, json=payload)
    response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
    print("Request successful.")
    print(response.json())  # レスポンスの内容を表示（JSON形式の場合）
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
