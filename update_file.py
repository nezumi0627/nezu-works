import json
import mimetypes
import os
import time
import urllib.parse
import uuid
from typing import Any, Dict, Optional, Tuple

import requests
from PIL import Image


class LineworksIconUpdater:
    """LINEWORKSのアイコンを更新するクラス"""

    def __init__(self, base_url: str = "https://talk.worksmobile.com"):
        """初期化

        Args:
            base_url: LINEWORKSのベースURL
        """
        self.base_url = base_url
        self.common_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Origin": "https://talk.worksmobile.com",
            "Referer": "https://talk.worksmobile.com/",
            "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
            "Host": "talk.worksmobile.com",
            "Device-Language": "ja_JP",
            "Priority": "u=1, i",
        }

    def _get_image_dimensions(
        self, image_path: str
    ) -> Tuple[Optional[int], Optional[int]]:
        """画像のサイズを取得する"""
        try:
            with Image.open(image_path) as img:
                return img.size
        except Exception as e:
            print(f"Error getting image dimensions: {str(e)}")
            return None, None

    def _upload_photo(
        self, image_path: str, cookies: Dict[str, str], xsrf_token: str
    ) -> Optional[str]:
        """写真をアップロードする"""
        try:
            url = "https://contact.worksmobile.com/v2/api/settings/profile/photo-upload"
            print(f"\nUploading photo to: {url}")

            # 画像のサイズを取得
            width, height = self._get_image_dimensions(image_path)
            if not width or not height:
                print("Failed to get image dimensions")
                return None
            print(f"Image dimensions: {width}x{height}")

            # ファイル情報の準備
            filename = os.path.basename(image_path)
            mime_type = (
                mimetypes.guess_type(image_path)[0] or "application/octet-stream"
            )
            filesize = os.path.getsize(image_path)
            print(f"File info: {filename} ({mime_type}, {filesize} bytes)")

            # セッションの作成と設定
            session = requests.Session()

            # 重要なクッキーを設定
            essential_cookies = {
                "WORKS_SES": cookies["WORKS_SES"],
                "NEO_SES": cookies["NEO_SES"],
                "NEO_CHK": cookies["NEO_CHK"],
                "WORKS_USER_ID": cookies["WORKS_USER_ID"],
                "XSRF-TOKEN": xsrf_token,
                "language": "ja_JP",
                "LC": "ja_JP",
                "WORKS_LOGIN_TYPE": "id",
                "TZ": "Asia/Tokyo",
                "timezone": "Asia/Tokyo",
                "WORKS_USER_DOMAIN": "ncorp",
                "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
            }

            for key, value in essential_cookies.items():
                session.cookies.set(key, value, domain=".worksmobile.com")

            # バウンダリーの生成
            boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:12]}"

            # ヘッダーの設定
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Origin": "https://contact.worksmobile.com",
                "Referer": "https://contact.worksmobile.com/v2/personal-info-settings/my",
                "X-Xsrf-Token": xsrf_token,
                "X-Login": cookies.get("WORKS_USER_ID", ""),
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Host": "contact.worksmobile.com",
                "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            }

            # マルチパートフォームデータを手動で構築
            boundary_bytes = f"--{boundary}".encode("utf-8")
            newline = b"\r\n"

            # ファイル名をURLエンコード
            encoded_filename = urllib.parse.quote(filename)

            # 各パートをバイト列として構築
            parts = []
            parts.append(boundary_bytes)
            parts.append(
                f'Content-Disposition: form-data; name="file"; filename="{encoded_filename}"'.encode(
                    "utf-8"
                )
            )
            parts.append(f"Content-Type: {mime_type}".encode("utf-8"))
            parts.append(b"")

            # ファイルの内容を読み込む
            with open(image_path, "rb") as f:
                file_content = f.read()

            # 全てのパーツを結合
            body = newline.join(parts) + newline + file_content + newline
            body += boundary_bytes + b"--" + newline

            # まず認証状態を確認
            check_session = session.get(
                "https://contact.worksmobile.com/v2/personal-info-settings/my",
                headers={k: v for k, v in headers.items() if k != "Content-Type"},
            )
            print(f"\nSession check status: {check_session.status_code}")

            # Content-Lengthを設定
            headers["Content-Length"] = str(len(body))

            # ファイルアップロード
            response = session.post(
                url,
                headers=headers,
                data=body,
                verify=True,
                timeout=30,
            )

            print(f"\nResponse status code: {response.status_code}")
            print("\nResponse headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")

            if response.status_code != 200:
                print(
                    f"Failed to upload photo: {response.status_code} - {response.text}"
                )
                return None

            photo_path = response.text.strip('"')
            print(f"\nReceived photo path: {photo_path}")
            return photo_path

        except Exception as e:
            print(f"Error in _upload_photo: {str(e)}")
            return None

    def _get_profile(self, cookies: Dict[str, str], xsrf_token: str) -> Optional[Dict]:
        """プロフィール情報を取得する"""
        try:
            url = "https://contact.worksmobile.com/v2/api/settings/profile"
            print(f"\nGetting profile from: {url}")

            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Origin": "https://contact.worksmobile.com",
                "Referer": "https://contact.worksmobile.com/v2/personal-info-settings/my",
                "X-Xsrf-Token": xsrf_token,
                "Host": "contact.worksmobile.com",
                "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Connection": "keep-alive",
            }

            # セッションの作成と設定
            session = requests.Session()

            # 重要なクッキーを設定
            essential_cookies = {
                "WORKS_SES": cookies["WORKS_SES"],
                "NEO_SES": cookies["NEO_SES"],
                "NEO_CHK": cookies["NEO_CHK"],
                "WORKS_USER_ID": cookies["WORKS_USER_ID"],
                "language": "ja_JP",
                "LC": "ja_JP",
                "WORKS_LOGIN_TYPE": "id",
                "TZ": "Asia/Tokyo",
                "timezone": "Asia/Tokyo",
                "WORKS_USER_DOMAIN": "ncorp",
                "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
                "XSRF-TOKEN": xsrf_token,
            }

            for key, value in essential_cookies.items():
                session.cookies.set(key, value, domain=".worksmobile.com")

            print("\nRequest headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")

            response = session.get(url, headers=headers)

            print(f"\nResponse status code: {response.status_code}")
            print("Response headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")

            if response.status_code != 200:
                print(
                    f"Failed to get profile: {response.status_code} - {response.text}"
                )
                return None

            profile = response.json()
            print(f"\nReceived profile: {json.dumps(profile, indent=2)}")

            # photoUrlを削除（自動的に設定される）
            if "photoUrl" in profile:
                del profile["photoUrl"]
                print("Removed photoUrl from profile")

            return profile

        except Exception as e:
            print(f"Error in _get_profile: {str(e)}")
            return None

    def _update_profile(
        self, profile: Dict, cookies: Dict[str, str], xsrf_token: str
    ) -> bool:
        """プロフィールを更新する"""
        try:
            url = "https://contact.worksmobile.com/v2/api/settings/profile"
            print(f"\nUpdating profile at: {url}")

            # セッションの作成と設定
            session = requests.Session()

            # 重要なクッキーを設定
            essential_cookies = {
                "WORKS_SES": cookies["WORKS_SES"],
                "NEO_SES": cookies["NEO_SES"],
                "NEO_CHK": cookies["NEO_CHK"],
                "WORKS_USER_ID": cookies["WORKS_USER_ID"],
                "language": "ja_JP",
                "LC": "ja_JP",
                "WORKS_LOGIN_TYPE": "id",
                "TZ": "Asia/Tokyo",
                "timezone": "Asia/Tokyo",
                "WORKS_USER_DOMAIN": "ncorp",
                "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
                "XSRF-TOKEN": xsrf_token,
            }

            for key, value in essential_cookies.items():
                session.cookies.set(key, value, domain=".worksmobile.com")

            # ヘッダーの設定
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Origin": "https://contact.worksmobile.com",
                "Referer": "https://contact.worksmobile.com/v2/personal-info-settings/my",
                "X-Xsrf-Token": xsrf_token,
                "Host": "contact.worksmobile.com",
                "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            }

            print("\nRequest headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")

            print(f"\nRequest body: {json.dumps(profile, indent=2)}")

            # プロフィールの更新
            response = session.put(
                url,
                headers=headers,
                json=profile,
                verify=True,
                timeout=30,
            )

            print(f"\nResponse status code: {response.status_code}")
            print("Response headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")

            if response.status_code not in [200, 204]:
                print(
                    f"Failed to update profile: {response.status_code} - {response.text}"
                )
                return False

            print("Profile updated successfully")
            return True

        except Exception as e:
            print(f"Error in _update_profile: {str(e)}")
            return False

    def _upload_file(
        self,
        file_path: str,
        cookies: Dict[str, str],
        xsrf_token: str,
        channel_no: int = 296519335,
        service_id: str = "works",
        max_retries: int = 3,
        retry_delay: int = 2,
    ) -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
        """ファイルをアップロードする"""
        for attempt in range(max_retries):
            try:
                # ファイルの種類を判定
                mime_type = (
                    mimetypes.guess_type(file_path)[0] or "application/octet-stream"
                )
                is_video = mime_type.startswith("video/")
                msg_type = 14 if is_video else 16  # 動画の場合は14、その他は16

                # 1. リソースパスの取得
                resource_url = f"{self.base_url}/p/oneapp/client/chat/issueResourcePath"

                filename = os.path.basename(file_path)
                filesize = os.path.getsize(file_path)

                resource_data = {
                    "serviceId": service_id,
                    "channelNo": channel_no,
                    "filename": filename,
                    "filesize": filesize,
                    "msgType": msg_type,
                    "channelType": 6,
                }

                headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                    "Content-Type": "application/json;charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    "Origin": "https://talk.worksmobile.com",
                    "Referer": "https://talk.worksmobile.com/",
                    "X-Xsrf-Token": xsrf_token,
                    "X-Ocn": "11",
                    "Device-Language": "ja_JP",
                }

                session = requests.Session()
                session.cookies.update(cookies)

                # リソースパス取得
                response = session.post(
                    resource_url,
                    json=resource_data,
                    headers=headers,
                    timeout=30,
                )

                if response.status_code != 200:
                    if attempt < max_retries - 1:
                        print(
                            f"Attempt {attempt + 1} failed, retrying in {retry_delay} seconds..."
                        )
                        time.sleep(retry_delay)
                        continue
                    return (
                        False,
                        f"Failed to get resource path: {response.status_code}",
                        None,
                    )

                resource_info = response.json()
                resource_path = resource_info.get("resourcePath")

                if not resource_path:
                    return False, "No resource path in response", None

                # 2. ファイルのアップロード
                upload_url = f"{self.base_url}/p/file{resource_path}"
                params = {
                    "Servicekey": service_id,
                    "writeMode": "overwrite",
                    "isMakethumbnail": "true",
                }

                # バウンダリーの生成
                boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:12]}"

                # X-Extrasの準備
                extras = {
                    "filesize": filesize,
                    "filename": filename,
                    "resourcepath": resource_path,
                }

                # 動画ファイルの場合、recordtimeを追加
                if is_video:
                    try:
                        import cv2

                        video = cv2.VideoCapture(file_path)
                        fps = video.get(cv2.CAP_PROP_FPS)
                        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
                        duration = frame_count / fps if fps > 0 else 0
                        extras["recordtime"] = duration
                        video.release()
                    except Exception as e:
                        print(f"Warning: Could not get video duration: {e}")

                upload_headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                    "Content-Type": f"multipart/form-data; boundary={boundary}",
                    "Origin": "https://talk.worksmobile.com",
                    "Referer": "https://talk.worksmobile.com/",
                    "X-Xsrf-Token": xsrf_token,
                    "X-Callerno": cookies.get("WORKS_USER_ID", "").split("-")[0],
                    "X-Channelno": str(channel_no),
                    "X-Serviceid": service_id,
                    "X-Resourcepath": resource_path,
                    "X-Extras": json.dumps(extras),
                    "X-Ocn": "1" if is_video else "11",
                    "X-Type": str(msg_type),
                    "X-Tid": str(int(time.time() * 1000)),
                    "Device-Language": "ja_JP",
                }

                # マルチパートフォームデータを手動で構築
                boundary_bytes = f"--{boundary}".encode("utf-8")
                newline = b"\r\n"

                # ファイル名をURLエンコード
                encoded_filename = urllib.parse.quote(filename)

                # 各パートをバイト列として構築
                parts = []
                parts.append(boundary_bytes)
                parts.append(
                    f'Content-Disposition: form-data; name="file"; filename="{encoded_filename}"'.encode(
                        "utf-8"
                    )
                )
                parts.append(f"Content-Type: {mime_type}".encode("utf-8"))
                parts.append(b"")

                # ファイルの内容を読み込む
                with open(file_path, "rb") as f:
                    file_content = f.read()

                # 全てのパーツを結合
                body = newline.join(parts) + newline + file_content + newline
                body += boundary_bytes + b"--" + newline

                upload_headers["Content-Length"] = str(len(body))

                # ファイルアップロード
                upload_response = session.post(
                    upload_url,
                    params=params,
                    headers=upload_headers,
                    data=body,
                    timeout=60,
                )

                if upload_response.status_code != 200:
                    if attempt < max_retries - 1:
                        print(
                            f"Attempt {attempt + 1} failed, retrying in {retry_delay} seconds..."
                        )
                        time.sleep(retry_delay)
                        continue
                    return (
                        False,
                        f"Failed to upload file: {upload_response.status_code}",
                        None,
                    )

                result = upload_response.json()

                if result.get("code") != 0:
                    return False, f"Upload failed: {result.get('message')}", None

                return True, None, result.get("result")

            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"Attempt {attempt + 1} failed with error: {str(e)}")
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    continue
                error_message = f"Error in file upload: {str(e)}"
                print(error_message)
                return False, error_message, None

        return False, "Max retries exceeded", None

    def update_icon(
        self, image_path: str, cookies: Dict[str, str], xsrf_token: str
    ) -> Tuple[bool, Optional[str]]:
        """アイコンを更新する

        Args:
            image_path: アイコン画像のパス
            cookies: 認証用クッキー
            xsrf_token: XSRF トークン

        Returns:
            Tuple[bool, Optional[str]]: (成功したかどうか, エラーメッセージ)
        """
        try:
            # 1. 画像をアップロード
            photo_path = self._upload_photo(image_path, cookies, xsrf_token)
            if not photo_path:
                return False, "Failed to upload photo"

            # 2. プロフィール情報を取得
            profile = self._get_profile(cookies, xsrf_token)
            if not profile:
                return False, "Failed to get profile"

            # 3. プロフィールを更新
            profile["photoPath"] = photo_path
            if not self._update_profile(profile, cookies, xsrf_token):
                return False, "Failed to update profile"

            return True, None

        except Exception as e:
            error_message = f"Error updating icon: {str(e)}"
            print(error_message)
            return False, error_message

    def remove_icon(
        self, cookies: Dict[str, str], xsrf_token: str
    ) -> Tuple[bool, Optional[str]]:
        """アイコンを削除する

        Args:
            cookies: 認証用クッキー
            xsrf_token: XSRF トークン

        Returns:
            Tuple[bool, Optional[str]]: (成功したかどうか, エラーメッセージ)
        """
        try:
            # 1. プロフィール情報を取得
            profile = self._get_profile(cookies, xsrf_token)
            if not profile:
                return False, "Failed to get profile"

            # 2. photoPathとphotoUrlを空に設定
            profile["photoPath"] = ""
            if "photoUrl" in profile:
                profile["photoUrl"] = ""

            # 3. プロフィールを更新
            if not self._update_profile(profile, cookies, xsrf_token):
                return False, "Failed to update profile"

            return True, None

        except Exception as e:
            error_message = f"Error removing icon: {str(e)}"
            print(error_message)
            return False, error_message


def update_icon(
    image_path: str, cookies: Dict[str, str], xsrf_token: str
) -> Tuple[bool, Optional[str]]:
    """アイコンを更新する

    Args:
        image_path: アイコン画像のパス
        cookies: 認証用クッキー
        xsrf_token: XSRF トークン

    Returns:
        Tuple[bool, Optional[str]]: (成功したかどうか, エラーメッセージ)
    """
    updater = LineworksIconUpdater()
    return updater.update_icon(image_path, cookies, xsrf_token)


def remove_icon(cookies: Dict[str, str], xsrf_token: str) -> Tuple[bool, Optional[str]]:
    """アイコンを削除する

    Args:
        cookies: 認証用クッキー
        xsrf_token: XSRF トークン

    Returns:
        Tuple[bool, Optional[str]]: (成功したかどうか, エラーメッセージ)
    """
    updater = LineworksIconUpdater()
    return updater.remove_icon(cookies, xsrf_token)
