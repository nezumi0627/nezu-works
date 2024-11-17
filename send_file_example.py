import json
import os
from typing import Dict

from update_file import LineworksIconUpdater

# クッキーを直接定義
COOKIES: Dict[str, str] = {
    "language": "ja_JP",
    "LC": "ja_JP",
    "WORKS_LOGIN_TYPE": "id",
    "TZ": "Asia/Tokyo",
    "timezone": "Asia/Tokyo",
    "WORKS_LOGIN_ID_LIST": "XLNbtSdhfPwCivAMf2wJOc2p39zHoxtY1Wb0R5Nf1f3lnI0fXCazSF2sXSWsiIoupp0Bk1nqR6QOVWBRbFasTjxkhf3dM4YDoRptfSK5Hp2Xnb0-0jOzS-Jl12zpQqnT",
    "debug": "false",
    "NNB": "IKEZZD5LTAPWO",
    "WORKS_RE_LOC": "jp1",
    "WORKS_TE_LOC": "jp1",
    "WORKS_USER_DOMAIN": "ncorp",
    "WORKS_USER_ID": "DjuIDxYieNq6heFUixPuqw",
    "NEO_SES": "AAABIB0sxx9TsMweHElEHYm/F/e5G4QJUVyZZDPnoaPnaCV0ePMlTmzb2yKniAOssKUcItzKqNuxz658vh9G+UKf4cFgYvNpYJ+k19q+9un+exw8UjRD0zSX9CzyzgZY91OnaT2HMtzfdhqnc4sW+BFgZlvZ+pBXTLLGvhNRhgb2davxL3DtgmYXXQ9Wz8DAodC+RLbb9lMk5QEaOQ2AJSB0DDSGDqJPo0JiKu30++RfpMuO8Pm7DJnBDJpA/uR7o9dIsyk1vGBnikaPLOTV82YLPx9a8QzRjDVs/mkMSwwJVSs9T2kiTxlJ3+mkf0TGQVzGowzY2ph1BY/8H0HfHcmAo4467xfX7nOdJEcpVFraTmRGrWgsDMVCcWrT3803Skka3Q==",
    "NEO_CHK": "AAAAYcevPopcpIa9TYLcdAL2uLVtaANvmmpYQN8UEbpsxvqU7mBQSZiURMOO2O62YRNcGi3RaqPJXcS4Cl20ZibulpCsXBkzMi1N2A2uK2S/7hu79cSN4NvIy4DH8d89nVkvLPLqZlrn5DXqTiL43wEL+4k=",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
    "WORKS_SES": "eJwVkLcRBEEIwFrCLSbE9l/S30cEMGKkUsU5eaBTU2j+OjItup74niGlZpHvRmukCPjzl0P4bhGMW0uS6oQGa5Ib8ANg1OKqCUcbx4JtqD5LIaFMFmLTJkFBWpeQxwEFH/02dpfm9RsvS28llJvi7m8exXQAOFv1QQMlzPpjcOu35LYrUvGyNV19ll3Fza7IAD8kCLmOlc3YBI1fJyzP/01/okFIpiGLB3c2fJ53UAG6VPPJCkF3MgVrrT1vO3XIq8Fs1tFmYkfdJ68+hQtKebOVncULFJ9OBAEg9A3nR/mWuWavpKWKE0fwGEj1C/eFDkQY/e6V2otRPL4KUD9g/2Xa",
}

# XSRFトークンを定義
XSRF_TOKEN = "76ee2f7b-cd85-4834-8c16-22833cbe7ee9"


def upload_file(
    file_path: str,
    cookies: Dict[str, str],
    xsrf_token: str,
    channel_no: int = 296519335,
    service_id: str = "works",
) -> bool:
    """ファイルをアップロードする

    Args:
        file_path: アップロードするファイルのパス
        cookies: 認証用クッキー
        xsrf_token: XSRFトークン
        channel_no: チャンネル番号
        service_id: サービスID

    Returns:
        bool: アップロードが成功したかどうか
    """
    try:
        print(f"Uploading file: {file_path}")

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        # クッキーにXSRFトークンを追加
        cookies_with_xsrf = cookies.copy()
        cookies_with_xsrf["XSRF-TOKEN"] = xsrf_token

        updater = LineworksIconUpdater()
        success, error, result = updater._upload_file(
            file_path=file_path,
            cookies=cookies_with_xsrf,
            xsrf_token=xsrf_token,
            channel_no=channel_no,
            service_id=service_id,
        )

        if not success:
            print(f"Upload failed: {error}")
            return False

        print("File uploaded successfully!")
        print(f"Upload result: {json.dumps(result, indent=2)}")
        return True

    except Exception as e:
        print(f"Error in upload_file: {str(e)}")
        return False


def main():
    """メイン処理"""
    try:
        # ファイルのアップロード
        file_path = "video.mp4"  # アップロードするファイルのパス
        if upload_file(file_path, COOKIES, XSRF_TOKEN):
            print("File upload completed successfully")
        else:
            print("File upload failed")

    except Exception as e:
        print(f"Error in main: {str(e)}")


if __name__ == "__main__":
    main()
