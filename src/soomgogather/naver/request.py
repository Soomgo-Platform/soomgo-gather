import time
import base64
import hashlib
import hmac
import requests

class RequestSearchAd:

    def __init__(self, base_url, api_key, secret_key, customer_id):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id

    # generate signature
    def generate(self, timestamp, method, uri):
        message = f"{timestamp}.{method}.{uri}"
        hash = hmac.new(bytes(self.secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)

        hash.hexdigest()
        return base64.b64encode(hash.digest())

    # naver_api_header
    def get_header(self, method, uri):
        timestamp = str(round(time.time() * 1000))
        signature = self.generate(timestamp, method, uri)

        return {
            'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp,
            'X-API-KEY': self.api_key,
            'X-Customer': str(self.customer_id),
            'X-Signature': signature,
            }
    
    # request by GET method
    def request_get(self, uri):
        method = 'GET'
        # parameter 존재 유무로 구분
        r = requests.get(self.base_url + uri, headers=self.get_header(method, uri))

        return r

    # request by POST method
    def request_post(self):

        return ""

    # request by DELETE method
    def request_delete(self):

        return ""