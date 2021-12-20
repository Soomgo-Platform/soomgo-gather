import requests_mock

from soomgogather.naver import StatReport

stat_report = StatReport(api_key='_', secret_key='_', customer_id='_')

url = stat_report.domain + stat_report.default_path
report_job_id = 'valid job id'


def test_statreport_list():
    with requests_mock.Mocker() as _mock:
        _mock.get(url, status_code=200, json='_')
        stat_report.list()
        assert _mock.called


def test_statreport_get():

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{url}/{report_job_id}', status_code=200, json='-')
        stat_report.get(report_job_id)

        assert _mock.called


def test_statreport_create():

    with requests_mock.Mocker() as _mock:
        _mock.post(url, status_code=201, json='_')
        stat_report.create(params={'report_type': 'AD_CONVERSION', 'report_date': '20211201'})
        assert _mock.called


def test_statreport_create_fail():

    try:
        stat_report.create(params={'report_date': '20211201'})
    except Exception as err:
        assert type(err) == ValueError


def test_statreport_delete_all():

    with requests_mock.Mocker() as _mock:
        _mock.delete(url, status_code=204, text='')
        stat_report.delete_all()
        assert _mock.called


def test_statreport_delete():

    with requests_mock.Mocker() as _mock:
        _mock.delete(f'{url}/{report_job_id}', status_code=204, text='')
        stat_report.delete(report_job_id)
        assert _mock.called
