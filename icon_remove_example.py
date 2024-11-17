#!/usr/bin/env python3
"""
LINEWORKSのアイコンを削除するスクリプト
"""

import sys
from typing import Dict

from update_file import remove_icon

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
    "NEO_CHK": "AAAAYF2m4YSPLNQvr8u2ZjuQWwR1WEvhqVnIt8uBDanQknUqyr6rYQWMFHNut8lMRp0HA6pD8tXI5qiyRKfzaCiZFK1LZysiHH4HARDiz1LuWi+D86Fk8SBguzP7jjuavpzkKQ==",
    "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE": "ja",
    "WORKS_SES": "eJwVz7cRBEEIAMGUUIswkfmH9PcWVRgDXao4Jw90agrNX0emRdcT3zOk1Czy3WiNFAF//nII3y2CcWtJUp3QYE1yA34BjFpcNeFo41iwDdVnKSSUyUJs2iQoSOsS8jig4Kvfxu7SvH7jZemthHJT3P3No5gOAGerPmighFl/DG79ltx2RSpetqarz7KruNkVGeCXBCHXsbIZm6Dx64Tl+Z/pDxqEZBqyeHBnw+d5BxWgSzUfVgi6kylYa+1526lDXg1ms442EzvqPnn1ES4o5c1WdhYvUHycCAJAuGJUhpgH9fGS8WYXelL2+4ZeKT8P3m9hYTjhEDYX1wJv+QdW52YG",
}

# XSRFトークン
XSRF_TOKEN = "55a6752f-9c08-4941-a5e8-d88ba8a7f397"


def main():
    """メイン処理"""
    try:
        # アイコンを削除
        success = remove_icon(COOKIES, XSRF_TOKEN)

        if success:
            print("Icon removed successfully")
            return 0
        else:
            print("Failed to remove icon")
            return 1

    except Exception as e:
        print(f"Error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
