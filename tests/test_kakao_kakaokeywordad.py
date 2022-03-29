import requests_mock

from soomgogather.kakao import KeywordReport


def test_refresh_token_success():
    k = KeywordReport(
        path='adAccounts',
        access_token='_',
        ad_account_id='_',
        user_refresh_token='vaild_rest_api_key',
        rest_api_key='vaild_rest_api_key',
    )
    with requests_mock.Mocker() as _mock:
        data = {
            'grant_type': 'refresh_token',
            'client_id': 'vaild_rest_api_key',
            'refresh_token': 'vaild_refresh_token',
        }

        _mock.post('https://kauth.kakao.com/oauth/token', status_code=200, json=data)
        k._refresh_token()
        assert _mock.called


def test_refresh_token_fail():
    k = KeywordReport(
        path='adAccounts',
        access_token='_',
        ad_account_id='_',
        user_refresh_token='invaild_rest_api_key',
        rest_api_key='invaild_rest_api_key',
    )
    try:
        k._refresh_token()

    except Exception as err:
        assert type(err) == ValueError


# def test_call_recursive():


# def test_refresh_token_fail_no_argument():
#     k = KeywordReport(
#         path='adAccounts',
#         access_token='_',
#         ad_account_id='_',
#     )
#     if all([k.user_refresh_token, k.rest_api_key]):
#         pass
#     else:
#         try:
#             k._refresh_token()
#         except Exception as err:
#             assert type(err) == ValueError


def test_refresh_token_success_file():
    print('file_save')


def test_refresh_token_fail_request():
    print('fail')


def test_refresh_token_fail_grant():
    print('grant')
