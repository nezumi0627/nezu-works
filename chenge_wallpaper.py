import requests

# リクエストURLとペイロード
url = 'https://talk.worksmobile.com/p/oneapp/client/chat/setChannelWallpaper'
payload = {
    "channelNo": 278287860,
    "wallpaper": "#ffff00"
}

# ヘッダー
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ja',
    'Cache-Control': 'no-cache',
    'Content-Encoding': 'gzip',
    'Content-Length': '47',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; language=ja_JP; WORKS_USER_DOMAIN=mouse; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; LC=ja_JP; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q; debug=false; NNB=M4DQ4RH7SNXGM; NEO_SES="AAABIcdKagY0gTs4n4Khnk1PNDsQwfPT4epZWlwMPS5IFE1dEVFp0B+OaTvsLIrvx0u+PCoYh6R/pknHTcFrGBIuYetBV4eyw1BSpJmAnPstbbbJUrvMPHASCe+YqXPqHlDFgWfhvPqwquWgnTZTNFcatJrvXJ/pDAGalCnOwNrahPQwwnKarvSC6F2/HlAScp7AsrDnt6TrPof/OfsM9z2eWzpWHPpMAQGlM8MV2UDMfLw+9q12sMhMZU1GMhHcjF+qK3XaxGGgyhaofJMj/H8IAlKzU9aomwbI9n9QeC1DDupLfM2lLdMwHLguZRvARDyxTwdVLp/vFbD2Ye4SMFmhc3O5Yta0MfJEMjFCLtDbNm9jytHPLN5fMT2BPVMg6rz/3nFiagaIdNCeiU2qitgk+Tw="; NEO_CHK="AAAAYc99UxITGaof2PkcP5ktTjcf4WfMkLu8s5XvG8LgAGDtzWthj57Lf2IJnNmr33BfPk3qMgSLh88Hnbi5SzZ5VyXHUkcgCAFomO90HQOmT0Wq0tjkNP24KsqFJ1DivwYADRjm+aauIO/UfUxWDx5zyTs="; WORKS_SES=eJwV0ccBA0EIA8CWyBxPYv8leV0AghFlhnOiYFNT6J92ZHp0qXx7jpSWRd9utEWKwKef5hDqLYJzW0lSndBgTXIDvgCMWlxz4WjnWPANM/UUEspkIXZrEszsPXub7iJD8ubKIpq7N9zYRRjO/fuQq2Oc1Cu2K72Fi1BCLEE1dDa7AnNhvZQ2yDXfDBNMP5cl6QyafkeldalLR/NdJyyPvax+0CAkt5DFgzsfvi/voAJsqeZhhaA7mYKt1vVrfwLIq8FstrFm4g9tVTTWmZ/P47D5Y63EY9kSPHyh3FnzojXmOZL/FWSD0O27O9d09MDxe8/54IEh8xWkeOs4jj/pimZO; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja',
    'Device-Language': 'ja_JP',
    'Origin': 'https://talk.worksmobile.com',
    'Priority': 'u=1, i',
    'Referer': 'https://talk.worksmobile.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Web-Device-Id': '110002509004447-e05b3f70-55d3-5a7b-8e10-d0cb47cc6b17',
    'X-Ocn': '11',
    'X-Request-Id': '110002509004447-e05b3f70-55d3-5a7b-8e10-d0cb47cc6b17-1719649646499-869-origin/v4.0',
    'X-Translate-Lang': 'ja'
}

try:
    # POSTリクエストを送信
    response = requests.post(url, json=payload, headers=headers)

    # ステータスコードの確認
    if response.status_code == 200:
        print("リクエスト成功！")
        print("レスポンス:")
        print(response.json())  # レスポンスのJSONを表示
    else:
        print(f"エラー: HTTP {response.status_code} - {response.reason}")

except requests.exceptions.RequestException as e:
    print(f"エラーが発生しました: {e}")
