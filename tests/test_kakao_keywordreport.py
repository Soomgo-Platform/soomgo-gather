import requests_mock

from soomgogather.kakao import KeywordReport

path = 'adAccounts'

k = KeywordReport(
    path=path,
    access_token='_',
    ad_account_id='_',
    user_refresh_token='_',
    rest_api_key='_',
    access_token_store_type='return',
)

params = {
    'metrics_groups': 'BASIC',
    'date_preset': 'TODAY',
}


def test_keywordreport_report_success():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{k.domain}/{path}/report', status_code=200, json={})
        assert k.report(params=params).status_code == 200


def test_refresh_token():
    with requests_mock.Mocker() as _mock:
        _mock.post('https://kauth.kakao.com/oauth/token', status_code=200, json={})
        if all([k.user_refresh_token, k.rest_api_key]):
            k._refresh_token()
            assert _mock.called


def test_wrong_parameters_fail():
    try:
        k.report(params={'metrics_groups': 'ERRORGROUP'})
    except Exception as err:
        assert type(err) == ValueError
