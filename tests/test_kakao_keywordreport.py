import os.path
from unittest.mock import Mock, mock_open, patch

import requests_mock

from soomgogather.kakao import KeywordReport

path = 'adAccounts'
params = {
    'metrics_groups': 'BASIC',
    'date_preset': 'TODAY',
}

k = KeywordReport(
    path=path,
    access_token='vaild_key',
    ad_account_id='_',
    user_refresh_token='_',
    rest_api_key='_',
)


def test_keywordreport_report_success():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{k.domain}/{path}/report', status_code=200, json={})
        assert k.report(params=params).status_code == 200


def test_keywordreport_report_success_with_401():
    with patch('soomgogather.kakao.keywordreport.KeywordReport._refresh_token') as mock:
        k = KeywordReport(
            path='adAccounts',
            access_token='invaild_key',
            ad_account_id='_',
            user_refresh_token='vaild_key',
            rest_api_key='vaild_key',
        )
        k.report(params={})
        mock.assert_called_once()


def test_wrong_parameters_fail():
    try:
        k.report(params={'abcd': 'ERROR'})
    except Exception as err:
        assert type(err) == ValueError
