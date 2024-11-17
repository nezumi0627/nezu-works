import requests

# リクエストURL
url = "https://sms-activate.org/stubs/handler_hstock.php"

# ヘッダー
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

# ボディ
data = {
    "action": "getGoods",
    "service": "go",
    "page": "1",
    "csrf": "6689cf7c3875d636c18f8e01fe6d56a6"
}

try:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    response_json = response.json()

    # dataからidが3881の要素を検索して取得
    item_3881 = next((item for item in response_json['data'] if item['id'] == 3881), None)

    if item_3881:
        print("ID:", item_3881["id"])
        print("Name:", item_3881["name"])
        print("Description:", item_3881["description"])
        print("Price:", item_3881["price"])
        print("Available:", item_3881["available"])
        print("Category:", item_3881["category_name"])
    else:
        print("Product with ID 3881 not found.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", str(e))


