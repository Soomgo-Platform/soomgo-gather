import base64
import hashlib
import hmac
import time

import marshmallow
import requests
from marshmallow import Schema, fields


class BaseSearchAD:
    domain = 'https://api.naver.com'

    allowed_method = ['GET', 'POST', 'DELETE', 'PUT']

    encode = 'utf-8'

    class HeaderSchema(Schema):
        content_type = fields.Str(data_key='Content-Type', default='application/json; charset=UTF-8')
        timestamp = fields.Str(data_key='X-Timestamp')
        api_key = fields.Str(data_key='X-API-KEY')
        customer = fields.Str(data_key='X-Customer')
        signature = fields.Str(data_key='X-Signature')

    def __init__(self, api_key, secret_key, customer_id):
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id
        self.timestamp = str(round(time.time() * 1000))

    def _generate_signature(self, method, path):
        _hash = hmac.new(
            bytes(self.secret_key, self.encode),
            bytes(f'{self.timestamp}.{method.upper()}.{path}', self.encode),
            hashlib.sha256,
        )
        _hash.hexdigest()
        return base64.b64encode(_hash.digest())

    def make_header(self, method, path):
        return self.HeaderSchema().dump(
            {
                'timestamp': self.timestamp,
                'api_key': self.api_key,
                'signature': self._generate_signature(method, path),
                'customer': self.customer_id,
            }
        )

    def call(self, method, path, params={}):
        return getattr(requests, method.lower())(
            self.domain + path, params=params, headers=self.make_header(method, path)
        )


class Bizmoney(BaseSearchAD):
    def status(self):
        return self.call('GET', '/billing/bizmoney')

    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(data_key='searchStartDt', required=True)
        search_end_dt = fields.Str(data_key='searchEndDt', required=True)

    def cost(self, params={}):
        return self.call('GET', '/billing/bizmoney/cost', params=self._BizmoneySchema().dump(params))

    def charge(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/charge', params=self._BizmoneySchema().dump(params))

    def exhaust(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/exhaust', params=self._BizmoneySchema().dump(params))

    def period(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/period', params=self._BizmoneySchema().dump(params))
