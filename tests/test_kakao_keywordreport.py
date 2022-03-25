import requests_mock

from soomgogather.kakao import KeywordReport

path = 'adAccounts'
k = KeywordReport(path=path, access_token='_', ad_account_id='_')

params = {
    'metrics_groups': 'BASIC',
    'date_preset': 'TODAY',
}


def test_keywordreport_report():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{k.domain}/{path}/report', status_code=200, json='_')
        assert k.report(params=params).status_code == 200
