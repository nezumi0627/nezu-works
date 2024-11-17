#!/usr/bin/env python3
"""
LINEWORKSのアイコンを更新するメインスクリプト
"""

import os
import sys
from typing import Dict

from update_file import update_icon

# 認証情報の設定
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

# XSRFトークン
XSRF_TOKEN = "55a6752f-9c08-4941-a5e8-d88ba8a7f397"


def print_usage():
    """使用方法を表示"""
    print("Usage:")
    print("  python main_icon.py [image_path]")
    print("")
    print("Arguments:")
    print("  image_path    アイコン画像のパス（オプション、デフォルト: icon.jpg）")
    print("")
    print("Example:")
    print("  python main_icon.py my_icon.jpg")


def main():
    """メイン処理"""
    # ヘルプ表示
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print_usage()
        return 0

    # コマンドライン引数から画像パスを取得
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = "images.jpg"  # デフォルトの画像パス

    # 画像が存在するか確認
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        print("")
        print_usage()
        return 1

    try:
        print(f"Updating icon with image: {image_path}")
        success = update_icon(image_path, COOKIES, XSRF_TOKEN)

        if success:
            print("Icon updated successfully!")
            return 0
        else:
            print("Failed to update icon")
            return 1

    except Exception as e:
        print(f"Error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
