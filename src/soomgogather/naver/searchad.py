import logging
from soomgogather.naver.request_searchad import RequestSearchAd

class Bizmoney(RequestSearchAd):

    def __init__(self, api_key, secret_key, customer_id, base_url='https://api.naver.com'):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id
        

    def get_report_period(self,start_dt, end_dt):
        uri = '/billing/bizmoney/histories/period'
        logging.info(f"Start requsting Daily BizMoney Status during period {start_dt} and {end_dt}")
        params={
            'searchStartDt': start_dt,
            'searchEndDt': end_dt,
        }
        r = self.request_get(self.base_url, uri, json_param=params)

        return r

            
    def get_report_cost(self, stat_dt, start_dt, end_dt):
        uri = '/billing/bizmoney/histories/cost'
        logging.info(f"Start requsting the used amount of bizmoney that day")
        params={
            'statDt': stat_dt,
            'searchStartDt': start_dt,
            'searchEndDt': end_dt,
        }
        r = self.request_get(self.base_url, uri, json_param=params)

        return r