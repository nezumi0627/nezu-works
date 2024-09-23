import requests
from colorama import Fore, init

# Coloramaを初期化
init(autoreset=True)

# ベースURL
JOIN = "https://join.worksmobile.com/jp/"


class WorksmobileAPI:
    def __init__(self, domain_id):
        self.domain_id = domain_id

    def _make_request(self, url, method, data=None):
        if method.upper() == "GET":
            response = requests.get(url, params=data)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        else:
            raise ValueError("Unsupported HTTP method")
        response.raise_for_status()  # エラーハンドリングのために追加
        return response.json()

    def get_blacklist_status(self):
        url = JOIN + "blacklist/ip/get"
        return self._make_request(url, "GET")

    def check_company_name(self, step_key, company_name):
        url = JOIN + f"joinup/v2/{step_key}/checkCompanyName"
        data = {"companyName": company_name}
        return self._make_request(url, "POST", data)

    def get_countries(self):
        url = JOIN + "joinup/v2/countrys"
        return self._make_request(url, "GET")

    def translate(self, step_key, company_name, last_name, first_name):
        url = JOIN + f"joinup/v2/{step_key}/translate"
        data = {"companyName": company_name, "lastName": last_name, "firstName": first_name}
        return self._make_request(url, "POST", data)

    def check_group_name(self, step_key, domain):
        url = JOIN + f"joinup/v2/{step_key}/groupName/check"
        data = {"domain": domain, "stepKey": step_key}
        return self._make_request(url, "POST", data)

    def get_password_level(self, password):
        url = JOIN + "v2/passwordGrade/getLevel"
        data = {"password": password}
        return self._make_request(url, "POST", data)

    def cache_domain(self, step_key, data):
        url = JOIN + f"joinup/v2/{step_key}/domains/cache"
        return self._make_request(url, "POST", data)

    def recaptcha(self, key):
        url = f"https://www.recaptcha.net/recaptcha/api2/reload?k={key}"
        data = {"k": key}
        return self._make_request(url, "POST", data)

    def email_auth(self, email, step_key, captcha_token):
        url = JOIN + f"joinup/v2/{step_key}/auth/type/email"
        data = {"email": email, "stepKey": step_key, "captchaToken": captcha_token}
        return self._make_request(url, "POST", data)

    def check_pin(self, mail, pin, step_key, captcha_token, auth_no_key):
        url = JOIN + f"joinup/v2/{step_key}/auth/type/email/check"
        data = {
            "email": mail,
            "authNo": pin,
            "authNoKey": auth_no_key,
            "stepKey": step_key,
            "captchaToken": captcha_token,
        }
        return self._make_request(url, "POST", data)

    def get_domains(self, step_key, data):
        url = JOIN + f"joinup/v2/{step_key}/domains"
        return self._make_request(url, "POST", data)

    def fingerprint(self, data):
        url = "https://auth.worksmobile.com/api/device/sns/fingerprint"
        return self._make_request(url, "POST", data)

    def get_properties(self):
        url = "https://contact.worksmobile.com/v2/api/main/properties"
        return self._make_request(url, "GET")


class WorksmobileAccountCreator:
    def __init__(self, api):
        self.api = api

    def create_account(self, step_key, company_name, last_name, first_name, password, email, pin, captcha_token):
        # ステップ 1: ドメインのチェック
        print(Fore.CYAN + "Checking domain...")
        domain_check_response = self.api.check_group_name(step_key, "aaaaaaaaaaaaaaa")
        print(Fore.GREEN + "Domain check response:", domain_check_response)

        # ステップ 2: 会社名のチェック
        print(Fore.CYAN + "Checking company name...")
        company_name_response = self.api.check_company_name(step_key, company_name)
        print(Fore.GREEN + "Company name check response:", company_name_response)

        # ステップ 3: 翻訳（必要に応じて）
        print(Fore.CYAN + "Translating...")
        translate_response = self.api.translate(step_key, company_name, last_name, first_name)
        print(Fore.GREEN + "Translate response:", translate_response)

        # ステップ 4: パスワードセキュリティのチェック
        print(Fore.CYAN + "Checking password security...")
        password_check_response = self.api.get_password_level(password)
        print(Fore.GREEN + "Password security check response:", password_check_response)

        # ステップ 5: ドメインのキャッシュ
        print(Fore.CYAN + "Caching domain...")
        cache_data = {
            "lastName": last_name,
            "regionCode": "REGION_1",
            "countryCode": "+81",
            "joinEnv": "PC",
            "domain": "aaaaaaaaaaaaaaa",
            "joinType": "B_WORKS",
            "businessTypeCode": "BIZ_TP01",
            "companyName": company_name,
            "joinAuthType": "EMAIL",
            "emailId": email,
            "firstName": first_name,
            "password": password,
            "domainId": self.api.domain_id,
        }
        cache_response = self.api.cache_domain(step_key, cache_data)
        print(Fore.GREEN + "Domain cache response:", cache_response)

        # ステップ 6: メール認証
        print(Fore.CYAN + "Authenticating email...")
        email_auth_response = self.api.email_auth(email, step_key, captcha_token)
        print(Fore.GREEN + "Email auth response:", email_auth_response)

        # ステップ 7: PINの確認
        print(Fore.CYAN + "Checking PIN...")
        pin_check_response = self.api.check_pin(email, pin, step_key, captcha_token, email_auth_response["sessionKey"])
        print(Fore.GREEN + "PIN check response:", pin_check_response)

        # ステップ 8: ドメインの取得
        print(Fore.CYAN + "Getting domains...")
        domains_data = {
            "lastName": last_name,
            "regionCode": "REGION_1",
            "countryCode": "+81",
            "joinEnv": "PC",
            "domain": "aaaaaaaaaaaaaaa",
            "joinType": "B_WORKS",
            "businessTypeCode": "BIZ_TP01",
            "companyName": company_name,
            "joinAuthType": "EMAIL",
            "emailId": email,
            "firstName": first_name,
            "password": password,
            "personalEmail": email,
            "domainId": self.api.domain_id,
            "captchaToken": captcha_token,
            "pagePath": "/jp/joinup-v3/step5-auth",
        }
        domains_response = self.api.get_domains(step_key, domains_data)
        print(Fore.GREEN + "Domains response:", domains_response)

        # ステップ 9: フィンガープリンティング
        print(Fore.CYAN + "Creating fingerprint...")
        fingerprint_data = {
            "userIdNo": "110002509337401",
            "domainId": self.api.domain_id,
            "tenantId": self.api.domain_id,
            "loginType": "login_web",
            "fingerPrint": "1a5136c6ed85b3e00b1b1f5f73b158fe",
            "language": "ja-JP",
            "fingerPrintDetail": "user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
            "email": email,
            "accessUrl": f"https://join.worksmobile.com/jp/joinup-v3/complete?stepKey={step_key}&domainId={self.api.domain_id}&isLoad=true",
        }
        fingerprint_response = self.api.fingerprint(fingerprint_data)
        print(Fore.GREEN + "Fingerprint response:", fingerprint_response)


# 使用例
api = WorksmobileAPI(domain_id="400495512")
creator = WorksmobileAccountCreator(api)

# ユーザーからの入力を取得
step_key = input(Fore.YELLOW + "Enter step key: ")
company_name = input(Fore.YELLOW + "Enter company name: ")
last_name = input(Fore.YELLOW + "Enter last name: ")
first_name = input(Fore.YELLOW + "Enter first name: ")
password = input(Fore.YELLOW + "Enter password: ")
email = input(Fore.YELLOW + "Enter email: ")
pin = input(Fore.YELLOW + "Enter PIN: ")
captcha_token = input(Fore.YELLOW + "Enter captcha token: ")

# アカウント作成の実行
creator.create_account(step_key, company_name, last_name, first_name, password, email, pin, captcha_token)
