import requests_mock

from soomgogather.naver import StatReport

api_key = "0100000000b47f8309b6e4c457716929c5b29d283ea13538a12391dbb9780b570970af5845"
secret_key = "AQAAAAC0f4MJtuTEV3FpKcWynSg+CU2VXAZjgpI0rmnttAJCrA=="
customer_id = "902486"

statreport = StatReport(api_key=api_key, secret_key=secret_key, customer_id=customer_id)

# params = {'item': 'Media'}

# list
# r = masterreport.list()
# print(type(r))
# # <class 'requests.models.Response'>
# print(r)
# print("RESPONSE")
# print(r.json())
# # <Response [200]>
# # print(r.headers)
# print("TEXT")
# print(r.text)
# print(r.text=='')
# print(r.json())
# # {'Connection': 'close', 'Cache-Control': 'no-store, must-revalidate', 'X-Transaction-ID': 'BTNO0MHK1HH9R', 'Content-Type': 'application/json;charset=UTF-8', 'Date': 'Wed, 15 Dec 2021 12:11:43 GMT', 'Strict-Transport-Security': 'max-age=15768000'}
# print(r.json())
# print(type(r.json()))
# # [{'id': '75F2A703309FC4AFA70FFA1046B39BAA', 'fromTime': '', 'item': 'Media', 'downloadUrl': 'https://api.naver.com/report-download?authtoken=VzqiQhlQR%2FLRHS%2BvtWqLup1o3LN%2BqBgmqG3zabVkMQbd3vC6pxVQcuvWIkbOZzed', 'updateTime': '2021-12-15T08:04:00Z', 'status': 'BUILT', 'managerLoginId': 'homepro', 'managerCustomerId': 902486, 'clientCustomerId': 902486, 'registTime': '2021-12-15T08:05:41.991Z'}]
# print(isinstance(r.json(), list))

# ### 만약 보고서 list가 없으면
# print(r)
# # <Response [204]>
# print(r.headers)
# # {'Cache-Control': 'no-store, must-revalidate', 'X-Transaction-ID': 'BTNOAB5K1DJED', 'Content-Type': 'application/json;charset=UTF-8', 'Date': 'Wed, 15 Dec 2021 12:32:47 GMT', 'Strict-Transport-Security': 'max-age=15768000'}
# print(r.status_code) # 204
# print(r.url) # https://api.naver.com/master-reports
# print(r.request) # <PreparedRequest [GET]>


### get
# report_job_id = '4B68F7637E7409700BAB6CB902BE1C33'
# # params = {'id': 'invalid id'}
# r = masterreport.get(job_id=report_job_id)
# print(r)
# # print(type(r.json()), r.json()) # <class 'dict'> {'id': '931CE6A0174E51E6E72A53A75BFD5814', 'fromTime': '', 'item': 'Media', 'downloadUrl': 'https://api.naver.com/report-download?authtoken=YlG%2B65ObrP7hxX88pAgytk80Yxo%2FCcs935TwMjOy%2BDaNabpLnncUwn6wPQv%2Bcpbp', 'updateTime': '2021-12-15T16:17:00Z', 'status': 'BUILT', 'managerLoginId': 'homepro', 'managerCustomerId': 902486, 'clientCustomerId': 902486, 'registTime': '2021-12-15T16:18:55.997Z'}
# print(r.status_code)  # 200
# # if invalid id
# print(r.status_code)  # 403
# # print(r.json()['title'] == 'Invalid Signature')
# print(r.json())


# # # delete
# r = masterreport.delete_all()
# print(type(r))
# # <class 'requests.models.Response'>
# print(r)
# # <Response [204]>
# print(r.headers)
# # {'Cache-Control': 'no-store, must-revalidate', 'X-Transaction-ID': 'BTNO4NMD9DIFQ', 'Content-Type': 'application/json;charset=UTF-8', 'Date': 'Wed, 15 Dec 2021 12:20:32 GMT', 'Strict-Transport-Security': 'max-age=15768000'}
# print(r.request)


## delete id
# report_job_id = '9A585FA9AD19D1355E474761585F6777'
# r = masterreport.delete(report_job_id)
# print(r) # <Response [204]>
# print(r.status_code) # 204
# print(r.text)
# print(r.request) # <PreparedRequest [DELETE]>
# print(r.json())


# create
# params = {'item': 'LabelRef', 'from_time': '2021-12-01T00:00:00Z'}
# params = {'item': 'A', 'from_time': '2021-12-01T00:00:00Z'}
# prams = []
params = {}
r = statreport.create(params=params)
print(r) # <Response [400]> # <Response [201]>
print(r.status_code) # 400 # 201
print(r.request) # <PreparedRequest [POST]> # <PreparedRequest [POST]>
print(r.url)
