<p align="center">
  <h1 align="center">Soomgo-gather</h1>
  <p align="center">Soomgo-gather는 (주)브레이브모바일에서 서비스 중인 <a href="https://soomgo.com/", target="_blank">숨고</a>
  에서 데이터 수집을 위해 구현한 통합 패키지입니다.</p> 
</p>

![PyPI - Python Version](https://img.shields.io/badge/python->=3.6-blue)
[![Coverage Status](https://coveralls.io/repos/github/Soomgo-Platform/soomgo-gather/badge.svg?branch=main)](https://coveralls.io/github/Soomgo-Platform/soomgo-gather?branch=main)
![Packagist License](https://img.shields.io/badge/license-MIT-green)

[comment]: <> (Soomgo-gather는 soomgo에서 데이터 수집을 위해 만든 외부 API 호출 통합 패키지이다.)

[comment]: <> (데이터 수집대상은 Naver SearchAd, Google Ads, Appsflyer 등이 포함될 예정이다.)

데이터 파이프라인을 구축하다보면 다양한 플랫폼에서 데이터를 수집해야하는 경우가 있습니다. 플랫폼마다 프로토콜도 다르고, API 명세도 일원화되지 않다보니 실제로 수집하기까지 오랜시간이 소요됩니다. 
또한, 대부분 수집을 위한 플랫폼들은 어느 조직이든 비슷합니다. 예로, 마케팅 데이터를 수집하기 위해서는 [GA](https://analytics.google.com/analytics/web/), 
[네이버검색광고시스템](https://searchad.naver.com/) 겠죠.

_Soomgo-gather_ 는 최소한의 시간으로 최대한 빨리 데이터를 수집할 수 있도록 심플한 인터페이스를 제공합니다.

---

**[Read the documentation on ReadTheDocs!](https://soomgo-gather.readthedocs.io/ko/latest/)**

---

## Supported platform

* [Naver Search AD](https://searchad.naver.com/)
    * [Bizmoney](https://naver.github.io/searchad-apidoc/#/tags/Bizmoney)  
    * [RelKwdStat](https://naver.github.io/searchad-apidoc/#/tags/RelKwdStat)
* [Google Search Console](https://search.google.com/search-console/about)

## Installation and usage

### Installation

_Soomgo-gather_ 는 `pip install soomgo-gather` 로 설치할 수 있고, Python 3.6 이상부터 지원하고 있습니다. 

### Usage

_Soomgo-gather_ 를 사용하는 방법은 간단합니다.

아래는 Naver Search AD.Bizmoney 를 수집하는 예시입니다.

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


## License

MIT

## Contributing

환영합니다! 프로젝트에 기여하고 싶다면 가이드를 읽어주세요.

방법은 어렵지 않습니다. 이슈를 생성하고, feature 브랜치에 작업하여 main 브랜치를 타겟으로 PR을 보내주시면 됩니다.

- [CONTRIBUTING.md](./CONTRIBUTING.md)

## Changelog

- [CHANGELOG.md](./CHANGELOG.md)


