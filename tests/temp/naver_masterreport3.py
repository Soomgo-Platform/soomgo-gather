import base64
import hashlib
import hmac
import json
import time

import requests
import signaturehelper as signaturehelper
from marshmallow import Schema, fields

DOMAIN = 'https://api.naver.com'
allowed_method = ['GET', 'POST', 'DELETE', 'PUT']
ENCODE = 'utf-8'

API_KEY = "0100000000b47f8309b6e4c457716929c5b29d283ea13538a12391dbb9780b570970af5845"
SECRET_KEY = "AQAAAAC0f4MJtuTEV3FpKcWynSg+CU2VXAZjgpI0rmnttAJCrA=="
CUSTOMER_ID = "902486"

report_type = 'Media'
params = {'reportTp': 'AD', 'statDt': '20211215'}

# naver_api_header
def get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)

    return {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Timestamp': timestamp,
        'X-API-KEY': API_KEY,
        'X-Customer': str(CUSTOMER_ID),
        'X-Signature': signature,
    }


def create_report(report_type, api_key, secret_key, customer_id, params):
    uri = '/stat-reports'
    method = 'POST'
    base_url = 'https://api.naver.com'

    r = requests.post(
        base_url + uri,
        json=params,
        headers=get_header(method, uri, api_key, secret_key, customer_id),
    )
    print(r)
    print(r.url)

    print(f"master-report create response status_code = {r.status_code}")  # 200 정상 호출
    r = r.json()
    print(f"response body\n{r}")

    return r


def delete_report(report_job_id, api_key, secret_key, customer_id):
    uri = f'/master-reports/{str(report_job_id)}'
    method = 'DELETE'
    base_url = 'https://api.naver.com'

    r = requests.delete(
        base_url + uri,
        headers=get_header(method, uri, api_key, secret_key, customer_id),
    )
    print(r)
    print(f"response status_code = {r.status_code}")
    print(r.text)
    print(r.request)
    # print(r.json())


def get_report(api_key, secret_key, customer_id, report_job_id=None):
    uri = '/master-reports'
    method = 'GET'
    base_url = 'https://api.naver.com'

    if report_job_id:
        uri = f'{uri}/{report_job_id}'

    r = requests.get(
        base_url + uri,
        headers=get_header(method, uri, api_key, secret_key, customer_id),
    )

    print(r)
    print(r.json())

    return r


def download_report(report_job_id, download_url, api_key, secret_key, customer_id):
    base_url = download_url
    uri = '/report-download'
    method = 'GET'

    r = requests.get(
        base_url,
        params={'Id': report_job_id},
        headers=get_header(method, uri, api_key, secret_key, customer_id),
    )
    print(r)
    print(type(r))
    # print(r.headers)
    # print(r.text)
    # print(r.content)

    return r


# create
r = create_report(
    report_type=report_type,
    api_key=API_KEY,
    secret_key=SECRET_KEY,
    customer_id=CUSTOMER_ID,
    params=params
)
# params={} master-report create response status_code = 400, r.json() -> {'code': 11001, 'message': '잘못된 파라미터 형식입니다.'}
# params= {} master-report create response status_code = 200, r.json() -> {'reportJobId': 1353504620, 'statDt': '2021-12-14T15:00:00Z', 'updateTm': '', 'reportTp': 'AD', 'status': 'REGIST', 'downloadUrl': '', 'regTm': '', 'loginId': 'homepro'}


# delete
# report_job_id = "DC803AAAC17F49FB5763BB0A043475E7"
# r = delete_report(report_job_id=report_job_id, api_key=API_KEY, secret_key=SECRET_KEY, customer_id=CUSTOMER_ID)

# report_job_id = "75F2A703309FC4AFA70FFA1046B39BAA"
# report_job_id = "-"

# get
# r = get_report(
#     api_key=API_KEY,
#     secret_key=SECRET_KEY,
#     customer_id=CUSTOMER_ID,
#     report_job_id=report_job_id
# )

# print(type(r))
# print(r)


# download_url
# r = {'id': '75F2A703309FC4AFA70FFA1046B39BAA', 'fromTime': '', 'item': 'Media', 'downloadUrl': 'https://api.naver.com/report-download?authtoken=qFDYF5XVjyB16u3P1spON5MgjacAT%2BhCK69a6zcvDomDrxIewXZsf%2BWgAhiV1v0M', 'updateTime': '2021-12-15T08:04:00Z', 'status': 'BUILT', 'managerLoginId': 'homepro', 'managerCustomerId': 902486, 'clientCustomerId': 902486, 'registTime': '2021-12-15T08:05:41.991Z'}
# download_url = r['downloadUrl']


# r = download_report(
#     report_job_id=report_job_id,
#     download_url=download_url,
#     api_key=API_KEY,
#     secret_key=SECRET_KEY,
#     customer_id=CUSTOMER_ID
#     )
print("###########")
print(r)
print(type(r))
