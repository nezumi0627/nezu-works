import requests
from bs4 import BeautifulSoup

url = "https://sms-activate.io/api/api.php"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://sms-activate.io",
    "Referer": "https://sms-activate.io/en/freePrice",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "lang=en; accept_cookie=no; g_state={\"i_l\":0}; sound=1; loyal_rank=0; isRetail=1; userid=10504720; refresh_token=ca724e09878c9cfa0c8a45d011752399; PHPSESSID=qmfis39347be7tvs9s3j9puorf; __cf_bm=lWtYyeGELfsHWAxKPMJWvOKM__3beVw.tIFWG9VTJvI-1719641906-1.0.1.1-Ja885_mVd1GqvP2nYPTCaRKnbUEuUOjf2IEBHVh0d.sV.HKkGkfGCkFWu4q9eCX3AGj79O.QmcQ8A2YTYzvpHA; session=e4b6230a82eab9c872a19cb6fad4f845; mobile=true; cf_clearance=4cLtoFl28_K.khzEBLIr56rcgpFMMgLi9T9nnWgbK2Q-1719642358-1.0.1.1-MqR38R48FajCr7oVrDUCCh.75PeMo3u.1CHSBs7B1Syjr4.uHF4w.V7dZumLABgb6ltpOwiyjKXHrhGGlO2ofQ"
}

data = {
    "act": "getBalance",
    "csrf": "a971807bd8c11545e30df1694471a489",
    "totals": "true"
}

try:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # エラーレスポンスを処理

    # BeautifulSoup を使用して HTML を解析
    soup = BeautifulSoup(response.text, 'html.parser')
    # 例えば、特定の要素を取得する場合はここで操作します
    print(soup.prettify())

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
except ValueError as e:
    print("Value Error:", e)
