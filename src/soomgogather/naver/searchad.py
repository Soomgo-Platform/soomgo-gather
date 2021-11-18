import requests
from soomgogather.naver.request import RequestSearchAd

class Bizmoney(RequestSearchAd):

    def __init__(self, api_key, secret_key, customer_id, base_url='https://api.naver.com'):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id
        

    def get_report_period(self,start_dt, end_dt):
        uri = '/billing/bizmoney/histories/period'
        r = requests.get(
            self.base_url + uri,
            params={
                'searchStartDt': start_dt,
                'searchEndDt': end_dt,
            },
            headers=self.get_header('GET', uri),
        )
        return r
