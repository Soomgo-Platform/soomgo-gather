# Soomgo-gather

![Packagist License](https://img.shields.io/badge/license-MIT-green)
![PyPI - Python Version](https://img.shields.io/badge/python->=3.6-blue)

Soomgo-gather는 soomgo에서 데이터 수집을 위해 만든 외부 API 호출 통합 패키지이다.

데이터 수집대상은 Naver SearchAd, Google Ads, Appsflyer 등이 포함될 예정이다.

---

## 패키지 구조

soomgogather 밑에 데이터 제공 대상 별(Naver, Google 등) 디렉토리 존재하고

데이터제공대상별 디렉토리 밑에 수집 데이터 별(Bizmoney, RelKwdStat 등) 파일 존재한다.  

*Sample*
* [soomgogather](./src/soomgogather)
  * [Naver](./src/soomgogather/naver)
    * [Bizmoney](./src/soomgogather/naver/bizmoney.py)


## 지원되는 데이터
* Naver SearchAd
    * Bizmoney
    * RelKwdStat
* Google Searchconsole
    * query
  
  
## 설치 방법

- 테스트 패키지 설치방법
```bash
pip install -e .[test]
```

## 사용 방법

1. 데이터 수집이 필요한 패키지를 import 한다.
2. 수집대상마다 요구하는 key를 셋팅하여 수집대상의 객체를 생성한다.
3. 필요한 함수를 호출하여 수집하려는 데이터를 받아온다.
4. 리턴된 HTTP response의 status_code를 확인하여 정상적으로 받아온 경우 response data를 사용한다.

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

**Version**: 1.0 (2021-11-23)


