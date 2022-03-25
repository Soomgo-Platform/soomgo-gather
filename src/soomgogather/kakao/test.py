# import requests

# domain = 'https://api.keywordad.kakao.com/openapi/v1'
# ACCESS_TOKEN = 'Ks33SRSmTCljdYhuR6dmgFxSGEJrS87DHD0iwgo9dRkAAAF_vYFvNg'
# AdAccountId = '407541'
# headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'AdAccountId': AdAccountId}
# path = 'adAccounts'

# a = getattr(requests, 'GET'.lower())(
#     domain + f'/{path}', headers=headers
# )

# print(a.status_code)
# print(a.json())
# print(a.headers)
# print(a.url)


# from _kakaokeywordad import BaseKakaoKeywordAD

# ACCESS_TOKEN = 'Ks33SRSmTCljdYhuR6dmgFxSGEJrS87DHD0iwgo9dRkAAAF_vYFvNg'
# AD_ACCOUNT = '407541'
# PATH = '/adAccounts/report'
# REFRESH = 'pi9lZuTLYI69y7sGjpy_1d8mTOq0F5C2_0IH1gorDNMAAAF_uqTsFQ'
# CLIENT = '6b1e8dc4105ef61f707d0675ff3ee368'
# access_token_store_type = 'file'

# a = BaseKakaoKeywordAD(access_token=ACCESS_TOKEN, ad_account_id=AD_ACCOUNT, refresh_token=REFRESH, client_id=CLIENT, access_token_store_type=access_token_store_type)
# a.call(method='GET', path=PATH, params={'metricsGroups': 'BASIC', 'dimension': 'HOUR'})


from soomgogather.kakao import KeywordReport

# ACCESS_TOKEN = 'FI_Meajyh-Vf2DriyzA65lDVo0oQAOdFDlTlUQopyV4AAAF_vaKr9Q'
# ACCESS_TOKEN = 'Ks33SRSmTCljdYhuR6dmgFxSGEJrS87DHD0iwgo9dRkAAAF_vYFvNg'
ACCESS_TOKEN = 'FI_Meajyh-Vf2DriyzA65lDVo0oQAOdFDlTlUQopyV4AAAF_vaKr9Q'
AD_ACCOUNT = '407541'
PATH = 'adAccounts'
REFRESH = 'pi9lZuTLYI69y7sGjpy_1d8mTOq0F5C2_0IH1gorDNMAAAF_uqTsFQ'
CLIENT = '6b1e8dc4105ef61f707d0675ff3ee368'
access_token_store_type = 'file'

k = KeywordReport(
    path=PATH,
    access_token=ACCESS_TOKEN,
    ad_account_id=AD_ACCOUNT,
    user_refresh_token=REFRESH,
    rest_api_key=CLIENT,
    access_token_store_type=access_token_store_type,
)
r = k.report(params={'metrics_groups': 'BASIC', 'dimension': 'HOUR', 'date_preset': 'YESTERDAY'})

print(r)
try:
    print(k.tokens)
except Exception as e:
    print(e)
    pass
print(r.json())
