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
    access_token='vaild_access_token',
    ad_account_id='_',
    user_refresh_token='_',
    rest_api_key='_',
)


def test_keywordreport_report_success():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{k.domain}/{path}/report', status_code=200, json={})
        assert k.report(params=params).status_code == 200


def test_wrong_parameters_fail():
    try:
        k.report(params={'abcd': 'ERROR'})
    except Exception as err:
        assert type(err) == ValueError
