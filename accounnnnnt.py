import json
import os
from urllib.parse import unquote

import requests


def manage_user_account(user_id):
    # ユーザーごとのアカウント生成数を読み込む
    def load_user_gen(user_id):
        file_path = f"user_{user_id}_gen.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        else:
            return {}

    # ユーザーごとのアカウント生成数を保存する
    def save_user_gen(user_id, user_gen):
        file_path = f"user_{user_id}_gen.json"
        with open(file_path, "w") as f:
            json.dump(user_gen, f)

    # バランスを取得する
    def get_balance():
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
            "Cookie": 'lang=en; accept_cookie=no; g_state={"i_l":0}; sound=1; loyal_rank=0; isRetail=1; userid=10504720; refresh_token=ca724e09878c9cfa0c8a45d011752399; PHPSESSID=qmfis39347be7tvs9s3j9puorf; __cf_bm=lWtYyeGELfsHWAxKPMJWvOKM__3beVw.tIFWG9VTJvI-1719641906-1.0.1.1-Ja885_mVd1GqvP2nYPTCaRKnbUEuUOjf2IEBHVh0d.sV.HKkGkfGCkFWu4q9eCX3AGj79O.QmcQ8A2YTYzvpHA; session=e4b6230a82eab9c872a19cb6fad4f845; mobile=true; cf_clearance=4cLtoFl28_K.khzEBLIr56rcgpFMMgLi9T9nnWgbK2Q-1719642358-1.0.1.1-MqR38R48FajCr7oVrDUCCh.75PeMo3u.1CHSBs7B1Syjr4.uHF4w.V7dZumLABgb6ltpOwiyjKXHrhGGlO2ofQ',
        }
        data = {
            "act": "getBalance",
            "csrf": "a971807bd8c11545e30df1694471a489",
            "totals": "true",
        }
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            json_response = response.json()
            balans_value = json_response.get("balans")
            return balans_value
        except requests.exceptions.RequestException as e:
            print("Request Error:", e)
            return None

    # アカウントを生成する
    def generate_account():
        url = "https://sms-activate.io/stubs/handler_hstock.php"
        payload = {
            "action": "buyProduct",
            "good_id": "37369",
            "csrf": "a971807bd8c11545e30df1694471a489",
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ja",
            "Content-Length": "69",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": 'lang=en; accept_cookie=no; g_state={"i_l":0}; sound=1; loyal_rank=0; isRetail=1; userid=10504720; refresh_token=ca724e09878c9cfa0c8a45d011752399; PHPSESSID=qmfis39347be7tvs9s3j9puorf; session=e4b6230a82eab9c872a19cb6fad4f845; mobile=true; cf_clearance=4cLtoFl28_K.khzEBLIr56rcgpFMMgLi9T9nnWgbK2Q-1719642358-1.0.1.1-MqR38R48FajCr7oVrDUCCh.75PeMo3u.1CHSBs7B1Syjr4.uHF4w.V7dZumLABgb6ltpOwiyjKXHrhGGlO2ofQ; __cf_bm=FmM9RiNHJkbh8Fw_VHnPuJdxmBjuz8DYbzzSZPBCLRU-1719642815-1.0.1.1-vln.z0sNGRDr2ECrR_l2cmBTVHghcZTmnUMdUGMYkk6UNES2WiyNu0i6d0JdvYjEh7OSG70nHAtXjwemtRkyDg',
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
        }
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            mail = response_json.get("mail")
            password = unquote(response_json.get("password"))
            submail = response_json.get("submail")
            return mail, password, submail
        else:
            print(f"Error: Status code {response.status_code}")
            return None, None, None

    # メイン処理
    user_gen = load_user_gen(user_id)
    balance = get_balance()
    mail, password, submail = generate_account()

    if mail and password and submail:
        user_gen[mail] = {"password": password, "submail": submail}
        save_user_gen(user_id, user_gen)
        return {
            "balance": balance,
            "account": {"mail": mail, "password": password, "submail": submail},
        }
    else:
        return {"balance": balance, "account": None}
