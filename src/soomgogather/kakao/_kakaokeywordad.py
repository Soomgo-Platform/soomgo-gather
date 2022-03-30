import json

import requests
from marshmallow import Schema, fields


class BaseKakaoKeywordAD:
    domain = 'https://api.keywordad.kakao.com'
    prefix_path = 'openapi'
    allowed_method = ['GET', 'POST', 'DELETE', 'PUT']

    class HeaderSchema(Schema):
        access_token = fields.Str(data_key='Authorization')
        ad_account_id = fields.Str(data_key='AdAccountId')

    def __init__(self, access_token, ad_account_id, api_version='v1', **kwargs):
        self.access_token = access_token
        self.ad_account_id = ad_account_id
        self.api_version = api_version

        if self.prefix_path:
            self.domain = f'{self.domain}/{self.prefix_path}/{self.api_version}'

        self.user_refresh_token = kwargs.get('user_refresh_token', None)
        self.rest_api_key = kwargs.get('rest_api_key', None)
        self.store_access_token = kwargs.get('store_access_token', True)

        if self.store_access_token:
            self.store_access_token_file = kwargs.get('store_access_token_file', 'tokens.json')

    def make_header(self):

        return self.HeaderSchema().dump(
            {'access_token': f'Bearer {self.access_token}', 'ad_account_id': self.ad_account_id}
        )

    def _refresh_token(self):
        """access token 갱신

        https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#refresh-token

        access token의 유효기간이 지난경우, client_id와 refresh_token을 사용해서
        access token을 갱신할 수 있도록 한다.
        """
        data = {'grant_type': 'refresh_token'}
        update_data = {
            'client_id': self.rest_api_key,
            'refresh_token': self.user_refresh_token,
        }
        update_data = {k: v for (k, v) in update_data.items() if v is not None}
        data.update(update_data)
        response = requests.post('https://kauth.kakao.com/oauth/token', data=data)

        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens.get('access_token', self.access_token)
            if self.store_access_token:
                with open(self.store_access_token_file, 'w') as fp:
                    json.dump(tokens, fp)
            return response
        else:
            raise ValueError(response.json())

    def call(self, method, path, params={}):

        r = getattr(requests, method.lower())(
            self.domain + path, json=params, params=params, headers=self.make_header()
        )

        return r
