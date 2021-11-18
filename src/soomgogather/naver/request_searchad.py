import time
import base64
import hashlib
import hmac
import requests
import logging

class RequestSearchAd:

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

    def request_get(self, base_url, uri, json_param={}):
        try:
            r = requests.get(
                base_url + uri,
                params=json_param,
                headers=self.get_header('GET', uri),
            )
            
            r.raise_for_status()

        except requests.exceptions.HTTPError as e:
            logging.exception(f"HTTP requests is failed {e}")
            raise RuntimeError("HTTP requests is failed.") 
             
        return r

