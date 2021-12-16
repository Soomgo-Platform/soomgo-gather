from google.ads.googleads.client import GoogleAdsClient
from marshmallow import Schema, ValidationError, fields, validate


class GoogleAds:
    """GoogleAds search_stream_request

    GoogleAds를 사용한다는 것은 GoogleAds의 API를 사용한다는 의미이기 때문에 Class 생성시 GoogleAds서비스까지 생성한다.

    query data 요청시 parameter는 다른 soomgo-gather와의 프로토콜을 동일하게 하기 위해 json 형식을 사용한다.

    Google developer key를 인스턴스의 기본설정 값(GOOGLE_ADS_CONFIGURATION_FILE_PATH)이나
    google developer 키파일(.yaml) 또는 dict를 사용하여 GoogleAds 서비스 객체를 생성한다.

    생성한 GoogleAds 인스턴스를 사용하여 쿼리를 통해 원하는 데이터에 대한 통계 정보를 얻을 수 있다.

    https://developers.google.com/google-ads/api/reference/rpc/v9/SearchGoogleAdsStreamRequest

    사용 예시) dict를 사용하여 GoogleAds 서비스 인스턴스를 생성한다.
    키워드 퍼포먼스의 어제 데이터의 클릭수를 받아온다.

    .. code-block:: python

        >>> from soomgogather.google import GoogleAds

        >>> customer_id = "123445678"
        >>> query = "SELECT metrics.clicks FROM keyword_view WHERE segments.date DURING YESTERDAY"

        >>> params = {
        ...     'query': query,
        ...     'customer_id': customer_id,
        >>> }

        >>> credentials_dict = {
        ...     'developer_token': '<<PUT YOUR DEVELOPER TOKEN>>',
        ...     'refresh_token': '<<PUT YOUR REFRESH TOKEN>>',
        ...     'client_id': '<<PUT YOUR CLIENT ID>>',
        ...     'client_secret': '<<PUT YOUR CLIENT SECRET>>',
        ...     'use_proto_plus': True,
        ...     'login_customer_id': '<<PUT YOUR LOGIN CUSTOMER ID>>',
        >>> }
        >>> # If using file
        >>> # credentials_dict = { 'key_file':'<<PUT YOUR KEY FILE(.yaml) PATH>>', }

        >>> service = GoogleAds(credentials=credentials_dict)
        >>> stream = service.search_stream_request(params)

        >>> for batch in stream:
        ...     for row in batch.results:
        ...         matrics = row.matrics
        ...         print(matrics.clicks)

    """

    def __init__(self, credentials=None, version="v8"):
        if credentials is None:
            self.client = self._create_client_from_default(version)
        elif 'key_file' in credentials:
            self.client = self._create_client_from_file(credentials.get('key_file'), version)
        else:
            self.client = self._create_client_from_dict(credentials, version)

        self.service = self.client.get_service("GoogleAdsService")

    class _GoogleAdsSchema(Schema):
        query = fields.Str(required=True)
        customer_id = fields.Str(required=True)
        summary_row_setting = fields.Str(
            validate=validate.OneOf(
                ['UNSPECIFIED', 'UNKNOWN', 'NO_SUMMARY_ROW', 'SUMMARY_ROW_WITH_RESULTS', 'SUMMARY_ROW_ONLY']
            )
        )

    def _get_params(self, params):
        if "summary_row_setting" in params:
            try:
                params["summary_row_setting"] = params["summary_row_setting"].upper()
            except ValidationError as err:
                raise ValueError(f"'summary_row_setting' is a string type.")
        try:
            return self._GoogleAdsSchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def _create_client_from_file(self, key_file, version):
        client = GoogleAdsClient.load_from_storage(path=key_file, version=version)
        return client

    def _create_client_from_dict(self, dict, version):
        client = GoogleAdsClient.load_from_dict(dict, version=version)
        return client

    def _create_client_from_default(self, version):
        client = GoogleAdsClient.load_from_storage(version=version)
        return client

    def search_stream_request(self, params):
        """전달한 필터와 조건에 맞는 GoogleAds 정보를 받아온다.

        **params:**
         - query: 데이터를 추출할 쿼리 (required)
         - customer_id: GoogleAds customer ID (required)
         - summary_row_setting: summary row에 대한 설정 (option)
                UNSPECIFIED : 명시되지 않음.
                UNKNOWN : 반환 요약 행의 unknown 값을 표시.
                NO_SUMMARY_ROW : 요약 행을 반환하지 않음.
                SUMMARY_ROW_WITH_RESULTS : 결과와 함께 요약 행을 반환. 요약 행은 마지막 배치에서만 반환(마지막 배치에는 결과가 포함되지 않음).
                SUMMARY_ROW_ONLY : 요약 행만 반환하고 결과는 반환하지 않음.
        """
        params = self._get_params(params)
        search_request = self.client.get_type("SearchGoogleAdsStreamRequest")
        search_request.customer_id = params.get('customer_id')
        search_request.query = params.get('query')

        if "summary_row_setting" in params:
            summary = getattr(
                self.client.get_type('SummaryRowSettingEnum').SummaryRowSetting, params.get('summary_row_setting')
            )
            search_request.summary_row_setting = summary.value

        stream = self.service.search_stream(search_request)

        return stream
