import base64
import hashlib
import hmac
import json
import time

import requests
from marshmallow import Schema, fields


class BaseSearchAD:
    domain = 'https://api.naver.com'

    allowed_method = ['GET', 'POST', 'DELETE', 'PUT']

    encode = 'utf-8'

    class HeaderSchema(Schema):
        content_type = fields.Str(data_key='Content-Type', dump_default='application/json; charset=UTF-8')
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
            self.domain + path, json=params, params=params, headers=self.make_header(method, path)
        )
