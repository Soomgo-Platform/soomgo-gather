import requests_mock

from soomgogather.naver import MasterReport

masterreport = MasterReport(api_key='_', secret_key='_', customer_id='_')

url = masterreport.domain + masterreport.default_path
job_id = 'valid job id'


def test_masterreport_list():
    with requests_mock.Mocker() as _mock:
        _mock.get(url, status_code=200, json='_')
        masterreport.list()
        assert _mock.called


def test_masterreport_get():

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{url}/{job_id}', status_code=200, json='-')
        masterreport.get(job_id)

        assert _mock.called


def test_masterreport_create():

    with requests_mock.Mocker() as _mock:
        _mock.post(url, status_code=201, json='_')
        masterreport.create(params={'item': 'AdExtension'})
        assert _mock.called


def test_masterreport_create_fail():

    try:
        masterreport.create(params={'from_time': '2021-12-01T00:00:00Z'})
    except Exception as err:
        assert type(err) == ValueError


def test_masterreport_delete_all():

    with requests_mock.Mocker() as _mock:
        _mock.delete(url, status_code=204, text='')
        masterreport.delete_all()
        assert _mock.called


def test_masterreport_delete():

    with requests_mock.Mocker() as _mock:
        _mock.delete(f'{url}/{job_id}', status_code=204, text='')
        masterreport.delete(job_id)
        assert _mock.called
