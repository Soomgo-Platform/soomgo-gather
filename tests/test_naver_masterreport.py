import requests_mock

from soomgogather.naver import MasterReport

masterreport = MasterReport(api_key='_', secret_key='_', customer_id='_')

url = masterreport.domain + masterreport.default_path
job_id = 'valid job id'


def test_masterreport_list():
    with requests_mock.Mocker() as _mock:
        _mock.get(url, status_code=200, json=[])
        masterreport.list()
        assert _mock.called


def test_masterreport_get():

    with requests_mock.Mocker() as _mock:
        _mock.get(
            f'{url}/{job_id}',
            status_code=200,
            json={
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
            )
        masterreport.get(job_id)

        assert _mock.called


def test_masterreport_create():

    with requests_mock.Mocker() as _mock:
        _mock.post(
            url,
            status_code=201,
            json={
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
            )
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
