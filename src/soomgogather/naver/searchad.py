import logging
import requests
from soomgogather.naver.request_searchad import RequestSearchAd

class Bizmoney(RequestSearchAd):

    def __init__(self, api_key, secret_key, customer_id, base_url='https://api.naver.com'):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id
        

    def get_report_period(self,start_dt, end_dt):
        uri = '/billing/bizmoney/histories/period'
        logging.info(f"Start requsting a bizmoney history during period {start_dt} and {end_dt}")

        try:
            r = requests.get(
                self.base_url + uri,
                params={
                    'searchStartDt': start_dt,
                    'searchEndDt': end_dt,
                },
                headers=self.get_header('GET', uri),
            )
            r.raise_for_status()

        except requests.exceptions.HTTPError as e:
            logging.exception(f"HTTP requests is failed {e}")
            raise RuntimeError("HTTP requests is failed.")  
        return r

