from marshmallow import Schema, ValidationError, fields, validate

from ._googleclient import BaseGoogleClient


class SearchConsole(BaseGoogleClient):
    """Google SearchConsol query

    인스턴스의 기본설정 값(GOOGLE_APPLICATION_CREDENTIALS)이나 service account 키파일을 사용하여 search console 서비스 객체를 생성하고
    사용자 사이트(site_url)의 검색 트래픽에 대한 통계 정보를 얻을 수 있다.

    https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query

    사용 예시) ``https://soomgo.com`` 에 대해 2021-11-30 ~ 2021-11-30까지 image 검색에 대한 통계정보를 받아온다.
    구글 API 서비스생성시 키파일을 사용하거나 인스턴스의 기본설정을 사용한다.

    .. code-block:: python

        >>> from soomgogather.google import SearchConsole

        >>> site_url = "https://soomgo.com"

        >>> service = SearchConsole('path/service_account_key.json')
        >>> # when using the default setting
        >>> # service = SearchConsole()

        >>> params = {
        ...     'start_dt': '2021-11-01',
        ...     'end_dt': '2021-11-30',
        ...     'type': 'image'
        ... }

        >>> r = service.query(site_url, params=params)

        >>> if r['rows']:
        ...     print(r['rows'])
    """

    scope = ['https://www.googleapis.com/auth/webmasters.readonly']
    service_name = 'searchconsole'
    service_version = 'v1'

    class _SearchConsoleSchema(Schema):
        start_dt = fields.Str(attribute='startDate', required=True)
        end_dt = fields.Str(attribute='endDate', required=True)
        dimensions = fields.List(
            fields.Str(),
            attribute='dimensions',
            validate=validate.ContainsOnly(['country', 'device', 'date', 'page', 'query', 'searchAppearance']),
        )
        row_limit = fields.Int(attribute='rowLimit', validate=validate.Range(max=25000))
        start_row = fields.Int(attribute='startRow', validate=validate.Range(min=0))
        type = fields.Str(
            attribute='type', validate=validate.OneOf(['web', 'video', 'image', 'news', 'googleNews', 'discover'])
        )
        dimension_filter_groups = fields.List(fields.Str(), attribute='dimensionFilterGroups')
        data_state = fields.Str(attribute='dataState', validate=validate.OneOf(['all', 'final']))
        aggregation_type = fields.Str(attribute='aggregationType')

    def _get_params(self, params):

        if "data_state" in params:
            params["data_state"] = params["data_state"].lower()

        try:
            return self._SearchConsoleSchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def query(self, site_url, params={}):
        """전달한 필터와 조건에 맞는 검색 트래픽에 대한 정보를 반환한다.

        :param params: search console의 데이터를 받아오기 위한 매개변수, start_dt, end_dt는 필수
        :type params: dict

        **params:**
            - *start_dt* (`str`) : 통계를 추출할 기간의 시작일, YYYY-MM-DD PT (UTC - 7:00/8:00) (required)
            - *end_dt* (`str`) : 통계를 추출할 기간의 종료일, YYYY-MM-DD PT (UTC - 7:00/8:00) (required)
            - *dimensions* (`list`) : 결과를 그룹핑할 키, 지정안하거나 여러개를 지정가능, 결과셋의 keys값
                - country, device, date, page, query, searchAppearance
            - *row_limit* (`int`) : 반환되는 결과의 row수 지정
                - default 1000, maximum = 25000
            - *start_row* (`int`) : 반환되는 결과의 시작 row 번호
                - 결과셋은 0부터 시작하는 인덱스
                - 양수만 가능
            - *type* (`str`) : 구글의 검색타입 필터
                - web(default), video, image, news, discover, googleNews(구글 뉴스 앱)
            - *dimension_filter_groups* (`list`) : dimensions 로 그룹핑시 필터 및 조건
                - groupType: 현재는 'and' 조건만 지원
                - filters: dimension의 필터 설정 리스트
                    - 형식: (dimension name) (an operator) (a value)
                    - dimension: 필터를 지정할 dimension 이름 (country, device, date, query, searchAppearance)
                    - operator: contains, equals, notEquals, includingRegex, excludingRegex
                    - expression: 필터 값
            - *data_state* (`str`) : all(fresh data 포함) 또는 final 값으로 지정 (대소문자 구분안함)
            - *aggregation_type* (`str`) : 결과의 aggregation(집합)타입, auto(default), byPage(by URI), byProperty(by property)
        """
        response = self.service.searchanalytics().query(siteUrl=site_url, body=self._get_params(params)).execute()
        return response
