import requests_mock

from soomgogather.naver import RelKwdStat

rel_keyword_stat = RelKwdStat(api_key='_', secret_key='_', customer_id='_')

params = {
    'hint_keywords': '숨고,soomgo',
}


def test_relkwdstat_list():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{rel_keyword_stat.domain}/keywordstool', status_code=200, json='_')

        assert rel_keyword_stat.list(params=params).status_code == 200


def test_relkwdstat_list_fail():
    params = {
        'hint_keywords': '숨고',
        'show_detail': 2,
    }

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{rel_keyword_stat.domain}/keywordstool', status_code=200, json='_')

        try:
            rel_keyword_stat.list(params=params)
        except Exception as err:
            assert type(err) == ValueError
