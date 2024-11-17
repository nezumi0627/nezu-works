import json
import mimetypes
import os
from typing import Dict, Optional, Tuple

import requests
from PIL import Image

# 定数定義
CALLER_NO = "110002509504044"
SERVICE_ID = "works"
MSG_TYPE = "11"
CHANNEL_TYPE = "6"


class LineworksImageSender:
    """LINEWORKSに画像を送信するクラス"""

    def __init__(self, base_url: str = "https://talk.worksmobile.com"):
        """初期化

        Args:
            base_url: LINEWORKSのベースURL
        """
        self.base_url = base_url
        self.common_headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Device-Language": "ja_JP",
            "X-Translate-Lang": "ja",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Origin": "https://talk.worksmobile.com",
            "Referer": "https://talk.worksmobile.com/",
        }

    def send_image(
        self, channel_no: int, image_path: str, cookies: Dict[str, str]
    ) -> bool:
        """画像を送信する

        Args:
            channel_no: チャンネル番号
            image_path: 送信する画像のパス
            cookies: 認証用クッキー

        Returns:
            bool: 送信成功ならTrue
        """
        try:
            # 画像のサイズを取得
            width, height = self._get_image_dimensions(image_path)
            if not width or not height:
                print("Failed to get image dimensions")
                return False

            # 1. リソースパスの取得
            resource_path = self._get_resource_path(channel_no, image_path, cookies)
            if not resource_path:
                return False

            # 2. 画像アップロード
            if not self._upload_image(
                channel_no, image_path, resource_path, cookies, width, height
            ):
                return False

            return True

        except Exception as e:
            print(f"Error sending image: {str(e)}")
            return False

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

    def _get_resource_path(
        self, channel_no: int, image_path: str, cookies: Dict[str, str]
    ) -> str:
        """リソースパスを取得する"""
        try:
            filename = os.path.basename(image_path)
            filesize = os.path.getsize(image_path)

            payload = {
                "serviceId": SERVICE_ID,
                "channelNo": channel_no,
                "filename": filename,
                "filesize": filesize,
                "msgType": int(MSG_TYPE),
                "channelType": int(CHANNEL_TYPE),
            }

            url = f"{self.base_url}/p/oneapp/client/chat/issueResourcePath"
            headers = self.common_headers.copy()

            response = requests.post(
                url, headers=headers, cookies=cookies, json=payload
            )

            if response.status_code != 200:
                print(
                    f"Failed to get resource path: {response.status_code} - {response.text}"
                )
                return ""

            data = response.json()
            if "resourcePath" not in data:
                print(f"Invalid response format: {data}")
                return ""

            return data["resourcePath"]

        except Exception as e:
            print(f"Error in _get_resource_path: {str(e)}")
            return ""

    def _upload_image(
        self,
        channel_no: int,
        image_path: str,
        resource_path: str,
        cookies: Dict[str, str],
        width: int,
        height: int,
    ) -> bool:
        """画像をアップロードする"""
        try:
            filename = os.path.basename(image_path)
            filesize = os.path.getsize(image_path)
            mime_type = (
                mimetypes.guess_type(image_path)[0] or "application/octet-stream"
            )

            # アップロード用のURLを構築
            upload_url = f"{self.base_url}/p/file{resource_path}"
            params = {
                "Servicekey": SERVICE_ID,
                "writeMode": "overwrite",
                "isMakethumbnail": "true",
            }

            # マルチパートフォームデータの準備
            files = {"file": ("blob", open(image_path, "rb"), mime_type)}

            # アップロード用ヘッダー
            upload_headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                "X-Callerno": CALLER_NO,
                "X-Channelno": str(channel_no),
                "X-Serviceid": SERVICE_ID,
                "X-Type": MSG_TYPE,
                "X-Resourcepath": resource_path,
                "X-Extras": json.dumps(
                    {
                        "filesize": filesize,
                        "filename": filename,
                        "resourcepath": resource_path,
                        "width": width,
                        "height": height,
                    }
                ),
            }

            response = requests.post(
                upload_url,
                headers=upload_headers,
                cookies=cookies,
                files=files,
                params=params,
            )

            if response.status_code != 200:
                print(
                    f"Failed to upload image: {response.status_code} - {response.text}"
                )
                return False

            return True

        except Exception as e:
            print(f"Error in _upload_image: {str(e)}")
            return False


def send_image_message(
    channel_no: int, image_path: str, cookies: Dict[str, str]
) -> bool:
    """画像メッセージを送信する

    Args:
        channel_no: チャンネル番号
        image_path: 送信する画像のパス
        cookies: 認証用クッキー

    Returns:
        bool: 送信成功ならTrue
    """
    sender = LineworksImageSender()
    return sender.send_image(channel_no, image_path, cookies)
