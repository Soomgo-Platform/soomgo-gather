from soomgogather.naver.searchad import Bizmoney
from datetime import datetime, timedelta

import requests_mock

def test_get_bizmoney():
    with requests_mock.Mocker() as mocker:
        mocker.get(requests_mock.ANY)
        TODAY_YMD = (datetime.now() + timedelta(hours=9)).strftime("%Y%m%d")
        
        bizmoney_report = Bizmoney('23xrtwr', 'aewErs35+CU2VXAZjgpI0rmnttAJCrA==', '93453', 'https://api.naver.com')
        r = bizmoney_report.get_report_period(TODAY_YMD,TODAY_YMD)
        
        assert r.status_code == 200

        r2 = bizmoney_report.get_report_cost(TODAY_YMD, TODAY_YMD,TODAY_YMD)
        assert r2.status_code == 200
