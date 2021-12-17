from marshmallow import Schema, ValidationError, fields, validate

from ._searchad import BaseSearchAD


class RelKwdStat(BaseSearchAD):
    """Naver SearchAd API RelKwdstat

    Naver SearchAd에서 API키를 발급받은 api_key, secret_key, customer_id를 사용하여 RelKwdStat 클래스 객체를 생성한다.
    생성한 RelKwdStat 객체를 사용하여 연관 검색어의 통계정보(Query count, Click count, CTR, 경쟁력 지표)에 대한 정보를 얻을 수 있다.

    http://naver.github.io/searchad-apidoc/#/tags/RelKwdStat

    사용 예시) 숨고와 숨고의 연관검색어에 대한 통계정보를 받아온다.

    .. code-block:: python

        >>> from soomgogather.naver import RelKwdStat

        >>> rel_keyword_stat = Relkwdstat(api_key='_', secret_key='_', customer_id='_')

        >>> r = rel_keyword_stat.list(params={
        ...    'hint_keywords' : '숨고,soomgo',
        ... })

        >>> if r.status_code == 200:
        ...     print(r.json())
    """

    class _RelkwdstatSchema(Schema):
        # 아래 다섯개중에 하나는 파라미터로 들어가야함
        site_id = fields.Str(attribute='siteId')
        biztp_id = fields.Int(attribute='biztpId')
        hint_keywords = fields.Str(attribute='hintKeywords')
        event = fields.Int(attribute='event')
        month = fields.Int(attribute='month')

        # 설정하지 않아도 defautl=0, _get_param 에서 입력받은 파라미터의 수를 확인하기 위해 명시적으로 0으로 설정
        show_detail = fields.Int(attribute='showDetail', validate=validate.OneOf([0, 1]))

    def _get_params(self, params):
        try:
            return self._RelkwdstatSchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def list(self, params={}):
        """파라미터의 조건에 맞는 키워드의 지표를 반환한다.

        :param params: 연관 검색어 데이터를 받아오기 위한 매개변수, ``show_detail`` 을 제외한 5개의 파라미터 중 1개 이상 지정되어야 결과값이 나옴
        :type params: dict

        **params:**
            - *site_id* (`str`) : 채널타입이 SITE인 비즈니스 채널 ID(nccBusinessChannelId)
            - *biztp_id* (`int`) :: 비즈니스 타입 ID
            - *hint_keywords* (`str`) : 검색어 - comma(,)로 구분하여 5개까지 가능, 공백 허용 안됨
                ex) ```soomgo, 숨고``` (X) ```soomgo,숨 고``` (X) ```soomgo,숨고``` (O)
            - *event* (`int`) : 시즌테마
                - https://gist.github.com/naver-searchad/235202ffb08f9433b6f7cb10e45875f7#file-seasonal_event_code-md
            - *month* (`int`) : 월
            - *show_detail* (`int`) : 상세정보 조회 여부
                - 0: 상세정보 조회안함(기본값)
                - 1: 상세정보 조회
        """
        return self.call('GET', '/keywordstool', params=self._get_params(params))
