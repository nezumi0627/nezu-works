import json

import requests

login_url = "https://auth.worksmobile.com/login/loginProcessV2"
data_url = "https://talk.worksmobile.com/p/contact/v3/domain/contacts/my"

inputId = "neko3desu4ne@nezumouse3"
password = "n@20080627"


def login():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": f"https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/&loginParam={inputId}",
        "Origin": "https://auth.worksmobile.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    }

    try:
        login_page_response = requests.get(
            "https://auth.worksmobile.com/login/login?accessUrl=https://talk.worksmobile.com/",
            headers=headers,
        )
        login_page_response.raise_for_status()

        payload = {
            "accessUrl": "https://talk.worksmobile.com/",
            "inputId": inputId,
            "password": password,
            "keepLoginYn": "N",
        }

        response = requests.post(
            login_url, headers=headers, data=payload, allow_redirects=False
        )

        print(f"ステータスコード: {response.status_code}")

        print("レスポンスヘッダー:")
        headers_json = json.dumps(dict(response.headers), indent=4, ensure_ascii=False)
        print(headers_json)

        print("\nレスポンスクッキー:")
        cookies_dict = {cookie.name: cookie.value for cookie in response.cookies}
        cookies_json = json.dumps(cookies_dict, indent=4, ensure_ascii=False)
        print(cookies_json)

        print("\nレスポンスボディ:")
        print(response.text)

        if response.status_code == 307:
            if "Location" in response.headers:
                redirect_url = response.headers["Location"]
                response = requests.get(
                    redirect_url,
                    headers=headers,
                    cookies=response.cookies,
                    allow_redirects=True,
                )
                response.raise_for_status()
                cookies = response.cookies
                return cookies
            else:
                print("リダイレクト URL が見つかりませんでした。")
                return None
        else:
            return response.cookies

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None


def fetch_data(cookies):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ja",
        "Device-Language": "ja_JP",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    response = requests.get(data_url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("結果がresult.jsonに保存されました。")
    else:
        print("リクエストが失敗しました。ステータスコード:", response.status_code)


def main():
    cookies = login()
    if cookies:
        fetch_data(cookies)


main()
