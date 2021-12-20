import base64
import hashlib
import hmac
import time

import requests
from marshmallow import Schema, fields


class HeaderSchema(Schema):
    content_type = fields.Str(data_key='Content-Type', dump_default='application/json; charset=UTF-8')
    timestamp = fields.Str(data_key='X-Timestamp')
    api_key = fields.Str(data_key='X-API-KEY')
    customer = fields.Str(data_key='X-Customer')
    signature = fields.Str(data_key='X-Signature')


DOMAIN = 'https://api.naver.com'
allowed_method = ['GET', 'POST', 'DELETE', 'PUT']
ENCODE = 'utf-8'

API_KEY = "0100000000b47f8309b6e4c457716929c5b29d283ea13538a12391dbb9780b570970af5845"
SECRET_KEY = "AQAAAAC0f4MJtuTEV3FpKcWynSg+CU2VXAZjgpI0rmnttAJCrA=="
CUSTOMER_ID = "902486"
TIMESTAMP = str(round(time.time() * 1000))


def _generate_signature(method, path):
    _hash = hmac.new(
        bytes(SECRET_KEY, ENCODE),
        bytes(f'{TIMESTAMP}.{method.upper()}.{path}', ENCODE),
        hashlib.sha256,
    )
    _hash.hexdigest()
    return base64.b64encode(_hash.digest())


def make_header(method, path):
    return HeaderSchema().dump(
        {
            'timestamp': TIMESTAMP,
            'api_key': API_KEY,
            'signature': _generate_signature(method, path),
            'customer': CUSTOMER_ID,
        }
    )


def call(method, path, params={}):
    return getattr(requests, method.lower())(DOMAIN + path, params=params, headers=make_header(method, path))


### GET '/master-reports'

path = '/stat-reports'
method = 'GET'

# r = call(method, path, params={})
# print(r)
# print(r.json())


### GET '/master-reports/' + str(report_job_id)
# r.json()['id']

# report_job_id = "75F2A703309FC4AFA70FFA1046B39BAA"
# print(report_job_id)
# path = f'/master-reports/{report_job_id}'


# create
params = {'reportTp': 'AD'}
r = call('POST', path, params=params)
print(r)

# get
# params = {'id': report_job_id}
# r = call('GET', path, params=params)

# delete
# params = {'id': report_job_id}
# print(params)
# r = call('DELETE', path, params=params)


# download_url
# data = [
#     {
#         'id': '75F2A703309FC4AFA70FFA1046B39BAA',
#         'fromTime': '',
#         'item': 'Media',
#         'downloadUrl': 'https://api.naver.com/report-download?authtoken=1QyJGTd%2FFbdvDh63om0wqovZY%2BoQp4G61xk5eg5bmuXydI4lfz0drxgE5H0%2BPCaB',
#         'updateTime': '2021-12-15T08:04:00Z',
#         'status': 'BUILT',
#         'managerLoginId': 'homepro',
#         'managerCustomerId': 902486,
#         'clientCustomerId': 902486,
#         'registTime': '2021-12-15T08:05:41.991Z',
#     }
# ]


# print(type(r))
# print(r)
# print(r.json())
