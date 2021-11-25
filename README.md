# Soomgo-gather
![Packagist License](https://img.shields.io/badge/license-MIT-green)
![PyPI - Python Version](https://img.shields.io/badge/python->=3.6-blue)

Soomgo-gather는 soomgo에서 데이터 수집을 위해 만든 외부 API 호출 통합 패키지이다.
데이터 수집대상은 Naver SearchAd, Google Ads, Appsflyer 등이 포함될 예정이다.

---
## 구조

└── soomgogather
    ├── 데이터제공대상(Naver, Google, Appsflyer)
    │   ├── 수집데이터 (Bizmoney)


## 설치 방법
- 테스트 패키지 설치방법
```bash
pip install -e .[test]
```

## 사용 방법
Usage:
```python
from soomgogather.naver import Bizmoney

bizmoney = Bizmoney(api_key='_', secret_key='_', customer_id='_')

r = bizmoney.exhaust(params={
    'search_start_dt': '20211118',
    'search_end_dt': '20211118',
 })

if r.status_code == 200:
     print(r.json())
```

**Version**: 0.1 (2021-11-25)


