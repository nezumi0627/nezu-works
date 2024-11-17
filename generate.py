import hashlib
import json
import os
import re
from datetime import datetime


def load_harfile(filepath):
    """HARファイルを読み込む関数"""
    with open(filepath, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    return har_data


def extract_requests(har_data):
    """HARファイルからリクエスト情報を抽出する関数"""
    requests = []
    for entry in har_data["log"]["entries"]:
        request = entry["request"]
        method = request["method"]
        url = request["url"]
        headers = {header["name"]: header["value"] for header in request["headers"]}
        post_data = request.get("postData", {}).get("text", None)
        requests.append(
            {"method": method, "url": url, "headers": headers, "post_data": post_data}
        )
    return requests


def generate_function_name(url):
    """URLから関数名を生成する関数"""
    return "request_" + re.sub(r"\W|^(?=\d)", "_", url)


def generate_file_name(request):
    """リクエスト情報からわかりやすいファイル名を生成する関数"""
    method = request["method"].lower()
    url = request["url"]
    # URLをハッシュ化してファイル名を短縮
    url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()
    # ファイル名に使えない文字を取り除く
    safe_url = re.sub(r"[^\w]", "_", url)
    return f"{method}_{url_hash}.py"


def generate_function_code(request):
    """リクエスト情報から関数コードを生成する関数"""
    func_name = generate_function_name(request["url"])
    method = request["method"].lower()
    url = request["url"]
    headers = request["headers"]
    post_data = request["post_data"]

    headers_code = f"headers = {headers}"
    post_data_code = f"data = '''{post_data}'''" if post_data else "data = None"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    function_code = f"""
import requests
def {func_name}():
    \"\"\"
    関数名: {func_name}
    リクエストタイプ: {method.upper()}
    引数: なし
    生成時間: {timestamp}
    @nezumi-project2024
    \"\"\"
    {headers_code}
    {post_data_code}
    response = requests.{method}(
        '{url}',
        headers=headers,
        data=data
    )
    return response
"""
    return function_code


def save_function_code(filename, code):
    """関数コードをファイルに保存する関数"""
    # 保存先のディレクトリを作成
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)


def main(harfile_path, output_dir):
    har_data = load_harfile(harfile_path)
    requests = extract_requests(har_data)

    for request in requests:
        func_code = generate_function_code(request)
        file_name = generate_file_name(request)
        filename = os.path.join(output_dir, file_name)
        save_function_code(filename, func_code)
        print(f"Saved: {filename}")


if __name__ == "__main__":
    harfile_path = "./autogen_har/talk.worksmobile.com.har"
    output_directory = "./autogen_har/defs"
    main(harfile_path, output_directory)
