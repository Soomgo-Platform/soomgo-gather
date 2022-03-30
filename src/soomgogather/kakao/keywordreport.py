from marshmallow import Schema, ValidationError, fields

from ._kakaokeywordad import BaseKakaoKeywordAD


class KeywordReport(BaseKakaoKeywordAD):
    """카카오 키워드광고 API 중 보고서 API 기능을 이용할 수 있다.
    https://developers.kakao.com/docs/latest/ko/keyword-ad/common#report

    해당 API 호출을 통해 광고계정 보고서, 캠페인 보고서 등에 대한 데이터를 수집할 수 있으며,
    보고서는 **집행한 광고의 결과를 항목별로 구성** 하여 확인할 수 있는 맞춤화된 보고서로 최근 2년간의 데이터를 제공한다고 한다.

    수집할 수 있는 지표는 다음에서 확인할 수 있다.
    https://developers.kakao.com/docs/latest/ko/keyword-ad/report#ad-account

    사용 예시)

    .. code-block:: python

        >>> from soomgogather.kakao import KeywordReport
        >>> access_token = '12345'
        >>> ad_account_id = 'AAAA'

        >>> # access token이 유효한 경우
        >>> k = KeywordReport(
        ...    path='adAccounts',
        ...    access_token=access_token,
        ...    ad_account_id=ac_account_id
        ...    )
        >>> params = {'metrics_groups': 'BASIC', 'dimension': 'HOUR'}
        >>> r = k.report(params=params)
        >>> if r.status_code == 200:
        ...     print(r.json())

        >>> # access token이 유효하지 않은 경우
        >>> user_refresh_token = 'XXX'
        >>> rest_api_key = 'YYY'
        >>> store_access_token = False
        >>> k = KeywordReport(
        ...    path='adAccounts',
        ...    access_token=access_token,
        ...    ad_account_id=ac_account_id
        ...    user_refresh_token=user_refresh_token,
        ...    rest_api_key=rest_api_key,
        ...    store_access_token=store_access_token,
        ... )

        >>> print(k.access_token) # 새로운 access token 저장

    """

    default_path = 'report'

    class _KeywordReportSchema(Schema):
        metrics_groups = fields.Str(attribute='metricsGroups', load_default='BASIC')
        start = fields.Str(attribute='start')
        end = fields.Str(attribute='end')
        date_preset = fields.Str(attribute='datePreset', load_default='TODAY')
        dimension = fields.Str(attribute='dimension')
        timeunit = fields.Str(attribute='timeUnit')

    def __init__(self, access_token, ad_account_id, path, **kwargs):
        super().__init__(access_token, ad_account_id, **kwargs)
        self.path = f'/{path}/{self.default_path}'

    def _get_params(self, params):
        try:
            params = self._KeywordReportSchema().load(params)
            return params
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def report(self, params={}):
        """보고서를 호출 할 때 params를 날려 맞춤화된 보고서를 구성할 수 있다.

        :param params: GET 요청 시 전달할 parameters 구성하여 전달
        :type params: dict

        https://developers.kakao.com/docs/latest/ko/keyword-ad/report#ad-account
        각 Paramer에 대해서는 kakao developers를 참고.
        Paramer를 Kakao API에서는 camel case로 지원하고 있으나, 파이썬에 친숙한 snake case로 변환하여 작업한다.

        파라미터 예시)

        **params**
            - *metrics_groups* (`str[]`) : metricsGroups 파라미터 (default BASIC)
            - *date_preset* (`str`) : datePreset 파라미터 (default TODAY)

        """
        r = self.call('GET', self.path, params=self._get_params(params))
        if r.status_code == 401:
            self._refresh_token()
            r = self.call('GET', self.path, params=self._get_params(params))
        return r
