soomgo-gather는 `Simple Versioning <https://simver.org//>`_ 을 준수합니다.

Simple Versioning 은 기본적으로 x.y 처럼 두 파트로 구성되고, 각 파트마다 아래의 규칙이 있습니다.

- Major(x): 변경사항이 이전 버전과 호환되지 않는 경우.
- Minor(y): 변경사항이 이전 버전과 호환되는 경우.

* Major 가 버전업이 되면 Minor 가 0으로 초기화한다.

이를 기준으로 soomgo-gather는 아래 규칙으로 버전관리를 합니다.

- Major(x): 새로운 수집 대상이 추가되는 경우. (ex. Naver SearchAd, Google search console, Google Ads, Facebook Business 등 )
- Minor(y): 기존 수집 대상의 하위 기능이 변경(추가,수정,삭제)되는 경우.

------------------------------------------------

Changes에는 총 5가지의 유형이 있습니다.

- New: 새로운 데이터 수집 기능 릴리즈.
- Changes: 기존에 배포된 기능의 변경.
- Deprecations: 기존에 배포된 기능중 더 이상 지원되지 않음.
- Doc only changes: 코드의 변경 없이 doc 만 수정.
- Contributors: 작업 참여자.


Version 1.3
-------------
released: 2021-12-22

**New**

- Naver SearchAd - StatReport 배포
- Naver SearchAd - MasterReport 배포
- Google Ads - stream_request 배포

**Contributors**

- Daisy Kim
- Paul Cho
- Rosa Kim

Version 1.2
-------------
released: 2021-12-07

**Changes**

- Google service name 변경

**Contributors**

- Rosa Kim

Version 1.1
-------------
released: 2021-12-06

**Doc only changes**

- pypi upload 변경

**Contributors**

- Paul Cho

Version 1.0
-------------
released: 2021-11-23

**New**

- Naver SearchAd - Bizmoney 배포
- Naver SearchAd - RelKwdStat 배포
- Google Searchconsole - query 배포

**Contributors**

- Paul Cho
- Rosa Kim