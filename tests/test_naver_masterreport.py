import pytest
import requests_mock

from soomgogather.naver import MasterReport

masterreport = MasterReport(api_key='_', secret_key='_', customer_id='_')

params = {'item': 'AdExtension'}
url = masterreport.domain + masterreport.default_path
job_id = 'valid job id'
invalid_job_id = 'invalid job id'


def test_masterreport_list():
    with requests_mock.Mocker() as _mock:
        _mock.get(url, status_code=200, json=[])
        r = masterreport.list()
        assert r.status_code == 200 and isinstance(r.json(), list)

        _mock.get(url, status_code=204, text='')
        r = masterreport.list()
        assert r.status_code == 204 and r.text == ''


def test_masterreport_get():
    return_value = {
        'id': 'valid job id',
        'fromTime': '',
        'item': 'AdExtension',
        'downloadUrl': 'https://api.naver.com/report-download?asdfasdfasdf',
        'updateTime': '2021-12-16T07:44:00Z',
        'status': 'BUILT',
        'managerLoginId': '-',
        'managerCustomerId': 000000,
        'clientCustomerId': 000000,
        'registTime': '2021-12-16T07:45:19.640Z',
    }

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{url}/{job_id}', status_code=200, json=return_value)
        r = masterreport.get(job_id)

        assert r.status_code == 200 and r.json()['id'] == job_id

    return_value = {'signature': '-', 'title': 'Invalid Signature', 'detail': "-", 'status': 403, 'type': '-'}

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{url}/{invalid_job_id}', status_code=403, json=return_value)
        r = masterreport.get(invalid_job_id)
        assert r.status_code == 403 and r.json()['title'] == 'Invalid Signature'


def test_masterreport_create():

    return_value = {
        'id': 'F54A7CBD8693E824858FCCD29A6FC6A3',
        'fromTime': '',
        'item': 'AdExtension',
        'downloadUrl': '',
        'updateTime': '',
        'status': 'REGIST',
        'managerLoginId': '-',
        'managerCustomerId': 000000,
        'clientCustomerId': 000000,
        'registTime': '2021-12-16T07:39:44.364Z',
    }

    with requests_mock.Mocker() as _mock:
        _mock.post(url, json=return_value, status_code=201)
        r = masterreport.create(params=params)
        assert r.status_code == 201 and r.json()['item'] == params['item']


def test_masterreport_create_fail():

    fail_params = {'from_time': '2021-12-01T00:00:00Z'}

    with pytest.raises(ValueError):
        masterreport.create(fail_params)


def test_masterreport_delete_all():

    with requests_mock.Mocker() as _mock:
        _mock.delete(url, status_code=204, text='')
        r = masterreport.delete_all()
        assert r.status_code == 204


def test_masterreport_delete():

    with requests_mock.Mocker() as _mock:
        _mock.delete(f'{url}/{job_id}', status_code=204, text='')
        delete_resp = masterreport.delete(job_id)

        _mock.get(f'{url}/{job_id}', status_code=204)
        get_resp = masterreport.get(job_id)
        assert delete_resp.status_code == 204 and get_resp.status_code == 204
