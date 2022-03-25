import json
import time

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
            print(self.domain)

        self.user_refresh_token = kwargs.get('user_refresh_token', None)
        self.rest_api_key = kwargs.get('rest_api_key', None)
        self.access_token_store_type = kwargs.get('access_token_store_type', None)

        if self.access_token_store_type == 'file':
            self.tokens_file = kwargs.get('access_token_store_file', 'tokens.json')

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
        if all([self.user_refresh_token, self.rest_api_key]):
            data = {
                'grant_type': 'refresh_token',
                'client_id': self.rest_api_key,
                'refresh_token': self.user_refresh_token,
            }
            print(f'Update ACCESS TOKEN from {self.access_token}')

            response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
            print(response)

            if response.status_code == 200:
                tokens = response.json()
                self.access_token = tokens.get('access_token', self.access_token)

                if self.access_token_store_type:
                    if self.access_token_store_type == 'file':
                        print(f'Save new access token to {self.tokens_file}')
                        with open(self.tokens_file, 'w') as fp:
                            json.dump(tokens, fp)
                    elif self.access_token_store_type == 'return':
                        print('Store new access tokens in variable self.tokens')
                        self.tokens = tokens
                    elif self.access_token_store_type is None:
                        print('Do not Save new access')
                        pass
            else:
                print('Please Check {"user_refresh_token": {USER_REFRESH_TOKEN}, "rest_api_key": {REST_API_KEY}}')

        else:
            print('Please Update {"user_refresh_token": {USER_REFRESH_TOKEN}, "rest_api_key": {REST_API_KEY}}')

    def call(self, method, path, params={}):
        r = getattr(requests, method.lower())(
            self.domain + path, json=params, params=params, headers=self.make_header()
        )
        print(r.url, r.status_code)

        if r.status_code == 401:
            print('Refresth Access Token')
            self._refresh_token()
            time.sleep(3)
            r = getattr(requests, method.lower())(
                self.domain + path, json=params, params=params, headers=self.make_header()
            )

        return r
