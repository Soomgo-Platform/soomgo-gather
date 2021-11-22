from soomgogather.naver import Bizmoney
import requests_mock

bizmoney = Bizmoney(api_key='_', secret_key='_', customer_id='_')
# bizmoney = Bizmoney(api_key='0100000000b47f8309b6e4c457716929c5b29d283ea13538a12391dbb9780b570970af5845', secret_key='AQAAAAC0f4MJtuTEV3FpKcWynSg+CU2VXAZjgpI0rmnttAJCrA==', customer_id='902486')

params = {
    'search_start_dt': '20211118',
    'search_end_dt': '20211118',
}


def test_bizmoney_status():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney', status_code=200, json='_')
        assert bizmoney.status().status_code == 200


def test_bizmoney_cost():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney/cost', status_code=200, json='_')

        assert bizmoney.cost(params=params).status_code == 200


def test_bizmoney_cost_fail():
    params = {
        'search_start_dt': '20211118',
    }

    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney/cost', status_code=200, json='_')
        
        try: 
            bizmoney.cost(params=params)
        except Exception as err:
            assert type(err) == ValueError

def test_bizmoney_charge():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney/histories/charge', status_code=200, json='_')
        assert bizmoney.charge(params=params).status_code == 200


def test_bizmoney_exhaust():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney/histories/exhaust', status_code=200, json='_')
        assert bizmoney.exhaust(params=params).status_code == 200


def test_bizmoney_period():
    with requests_mock.Mocker() as _mock:
        _mock.get(f'{bizmoney.domain}/billing/bizmoney/histories/period', status_code=200, json='_')
        assert bizmoney.period(params=params).status_code == 200
