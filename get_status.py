from datetime import datetime, timezone

import requests


def date_to_timestamp_ms(date_str):
    """
    Convert a date string in the format 'YYYY-MM-DD' to a millisecond timestamp.

    Args:
        date_str (str): The date string in the format 'YYYY-MM-DD'.

    Returns:
        int: The timestamp in milliseconds.
    """
    date_time = datetime.strptime(date_str, "%Y-%m-%d")
    timestamp_ms = int(date_time.timestamp() * 1000)
    return timestamp_ms


def send_request_with_date(date_str):
    """
    Send a GET request to the specified URL with the timestamp of the given date.

    Args:
        date_str (str): The date string in the format 'YYYY-MM-DD'.
    """
    timestamp_ms = date_to_timestamp_ms(date_str)

    url = f"https://dashboard.worksmobile.com/jp/api/v2/issueDetail?date={timestamp_ms}&language=ja_JP"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            data = response.json()
            issues = data.get("data", [])

            for issue in issues:
                contents = issue.get("contents", [])

                # status 4 が存在するかどうかを確認
                has_resolved = any(content.get("status") == 4 for content in contents)

                for content in contents:
                    status = content.get("status")
                    content_message = content.get("content")

                    if status == 1:
                        status_message = "確認中"
                    elif status == 2:
                        status_message = "進行中"
                    elif status == 4:
                        status_message = "復旧完了"
                    else:
                        status_message = "不明"

                    # すでに復旧完了している場合、復旧完了の後に発生した問題だけを表示
                    if has_resolved and status != 4:
                        continue

                    print(f"コンテンツ: {content_message}")
                    print(f"状態: {status_message}")

                    timestamp_ms = content.get("time")
                    if timestamp_ms:
                        formatted_date = convert_timestamp_to_date(timestamp_ms)
                        print(f"発生時間: {formatted_date}")
                    print()  # 空行を挿入して読みやすくする

        else:
            print(f"エラー: ステータスコード {response.status_code}")

    except requests.RequestException as e:
        print(f"リクエストエラー: {e}")


def convert_timestamp_to_date(timestamp_ms):
    """
    Convert a millisecond timestamp to a readable date format.

    Args:
        timestamp_ms (int): The timestamp in milliseconds.

    Returns:
        str: The formatted date string.
    """
    timestamp_s = timestamp_ms / 1000
    date_time = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)
    return date_time.strftime("%Y-%m-%d %H:%M:%S")


# 指定された日付でリクエストを送信
send_request_with_date("2024-07-31")
