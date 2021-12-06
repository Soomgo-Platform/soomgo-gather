from soomgogather.google import SearchConsole

params = {
    'start_dt': '2021-11-23',
    'end_dt': '2021-11-23',
    'dimensions': ['page', 'date', 'query', 'device'],
    'start_row': 0,
    'row_limit': 10,
    'data_state': 'ALL',
}

site_url = "https://soomgo.com"

mock_response = {
    'rows': [
        {
            'keys': ['https://soomgo.com/test_mock', '2021-11-01', '악기', 'DESKTOP'],
            'clicks': 1,
            'impressions': 1,
            'ctr': 1,
            'position': 2,
        }
    ],
    'responseAggregationType': 'byPage',
}


def _create_service_from_file(mocker):
    mocker.patch('google.oauth2.service_account.Credentials.from_service_account_file', return_value=None)
    mocker.patch('google.auth.default', return_value=[None, None])

    service = SearchConsole('service_account_key.json')

    assert service
    return service


def _create_service_from_default(mocker):
    mocker.patch('google.auth.default', return_value=[None, None])

    service = SearchConsole()

    assert service
    return service


def test_search_console_query_file(mocker):
    mocker.patch('googleapiclient.http.HttpRequest.execute', return_value=mock_response)
    service = _create_service_from_file(mocker)
    r = service.query(site_url, params=params)

    assert r['responseAggregationType']


def test_search_console_query_default(mocker):
    mocker.patch('googleapiclient.http.HttpRequest.execute', return_value=mock_response)

    service = _create_service_from_default(mocker)
    r = service.query(site_url, params=params)
    assert r['responseAggregationType']


def test_search_console_query_fail(mocker):
    mocker.patch('googleapiclient.http.HttpRequest.execute', return_value=mock_response)
    params = {'start_dt': '2021-11-23'}
    service = _create_service_from_default(mocker)

    try:
        service.query(site_url, params=params)
    except Exception as err:
        assert type(err) == ValueError
