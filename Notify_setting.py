import requests

def NotifySetting(mode):
    """
    silentMode
    0: Notify
    1: silentNotify
    2: Notifications only for talks where is mentioned
    
    """
    url = 'https://talk.worksmobile.com/p/oneapp/client/chat/silentMode'
    
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie': 'WORKS_RE_LOC=jp1; WORKS_TE_LOC=jp1; WORKS_LOGIN_TYPE=id; TZ=Asia/Tokyo; timezone=Asia/Tokyo; language=ja_JP; WORKS_USER_DOMAIN=mouse; WORKS_USER_ID=ETDxRmA0AzLNTOsITBtjxYvCq3cmJZ32C8jdyJAjcmw; LC=ja_JP; WORKS_LOGIN_ID_LIST=XLNbtSdhfPwCivAMf2wJORuOytTzmhjzZZLNSnrjEfDgCTHh3NnoiX8dMo5hgzNH304H5t3-j7bZlsj5VqgPRKbvIvH0KEpycGrUvQWi_56hVcNUbzSeSMb1CZgGFq6Q; debug=false; NNB=M4DQ4RH7SNXGM; NEO_SES="AAABIcdKagY0gTs4n4Khnk1PNDsQwfPT4epZWlwMPS5IFE1dEVFp0B+OaTvsLIrvx0u+PCoYh6R/pknHTcFrGBIuYetBV4eyw1BSpJmAnPstbbbJUrvMPHASCe+YqXPqHlDFgWfhvPqwquWgnTZTNFcatJrvXJ/pDAGalCnOwNrahPQwwnKarvSC6F2/HlAScp7AsrDnt6TrPof/OfsM9z2eWzpWHPpMAQGlM8MV2UDMfLw+9q12sMhMZU1GMhHcjF+qK3XaxGGgyhaofJMj/H8IAlKzU9aomwbI9n9QeC1DDupLfM2lLdMwHLguZRvARDyxTwdVLp/vFbD2Ye4SMFmhc3O5Yta0MfJEMjFCLtDbNm9jytHPLN5fMT2BPVMg6rz/3nFiagaIdNCeiU2qitgk+Tw="; NEO_CHK="AAAAYeqAJvPpvDt1+zPSy6uNEFt3L2n/y8wHlb5MAF1bwdr1/3RpAbRfLvaX1Uj2xSLtymvkK5DW+4iHIFpVYdDIj9gHMx1JQDKd0WyFbUQESsfbbSNLPqpDrSOMTlIx3HmPWA+sJfbc0bQwh23VQoh6Xu0="; WORKS_SES=eJwN0MkBAEEEAMGU3McTQ/4h7QagKW2G70TBXr9GD52s8pxWiT1HKqum2M2xLBEIDa1HqLcIzmMtRX1CD/sVD+AfwOzFNRfOcc4F3zRTLyGhKhZityHBqtmzf9NdVkrdu7bM4ZlNN3YRhnOPQO7J56TeudPlI9yEkmIFqqlvazqxFtZbaZNc659hgje/y4r0PTSNo9a+0qWjFzcFy8/+1vzQJCS3lMWDO398UXfQCbbU78cKwUwxJVuva4z/AqjrhzVsz4aJA21VNNeZf5/n4XCwduGxbAse/tEOOowM+09mqr+PP9l+HjHtf5DT1PjQwv1PDHQAtAtwEy2GD93YZew=; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=ja'
    }
    
    payload = {
        "silentMode": mode,
        "channelNo": 278287860,
        "serviceId": "works",
        "userNo": 110002509004447
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for bad response status
        print('Status Code:', response.status_code)
        print('Response JSON:', response.json())
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
NotifySetting(0)
