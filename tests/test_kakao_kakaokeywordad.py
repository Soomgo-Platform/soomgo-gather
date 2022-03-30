import requests_mock

from soomgogather.kakao import KeywordReport


def test_refresh_token_success():
    k = KeywordReport(
        path='adAccounts',
        access_token='_',
        ad_account_id='_',
        user_refresh_token='vaild_key',
        rest_api_key='vaild_key',
    )
    with requests_mock.Mocker() as _mock:
        data = {
            'grant_type': 'refresh_token',
            'client_id': 'vaild_key',
            'refresh_token': 'vaild_key',
        }

        _mock.post('https://kauth.kakao.com/oauth/token', status_code=200, json=data)
        k._refresh_token()
        assert _mock.called


def test_refresh_token_fail():
    k = KeywordReport(
        path='adAccounts',
        access_token='_',
        ad_account_id='_',
        user_refresh_token='invaild_key',
        rest_api_key='invaild_key',
    )
    try:
        k._refresh_token()

    except Exception as err:
        assert type(err) == ValueError
