from marshmallow import Schema, ValidationError, fields

from ._searchad import BaseSearchAD


class Bizmoney(BaseSearchAD):
    """Naver SearchAd API Bizmoney

    Naver SearchAd에서 API키를 발급받은 api_key, secret_key, customer_id를 사용하여 Bizmoney 클래스 객체를 생성한다.
    생성한 Bizmoney 객체로 Bizmoney의 잔액, 사용금액, 충전내역, 잠금상태에 대한 정보를 얻을 수 있다.

    http://naver.github.io/searchad-apidoc/#/tags/Bizmoney

    사용 예시) 2021-11-18 에 사용한 금액을 받아온다.

    .. code-block:: python

        >>> from soomgogather.naver import Bizmoney

        >>> bizmoney = Bizmoney(api_key='_', secret_key='_', customer_id='_')

        >>> r = bizmoney.exhaust(params={
        ...    'search_start_dt': '20211118',
        ...    'search_end_dt': '20211118',
        ... })

        >>> if r.status_code == 200:
        ...     print(r.json())
    """

    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(attribute='searchStartDt', required=True)
        search_end_dt = fields.Str(attribute='searchEndDt', required=True)
        stat_dt = fields.Str(attribute='statDt')

    def _get_params(self, params):
        try:
            return self._BizmoneySchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def status(self):
        """Bizmoney 잔액과 환불/예산의 잠금상태를 반환한다."""
        return self.call('GET', '/billing/bizmoney')

    def cost(self, params={}):
        """파라미터로 전달한 기간의 Bizmoney 사용된 금액을 반환한다.

        :param params: 사용금액 데이터를 받아오기 위한 매개변수,  search_start_dt, search_end_dt 모두 필수
        :type params: dict

        **params:**
            - *search_start_dt* (`str`) : 조회 시작일, YYYYMMDD (KST)
            - *search_end_dt* (`str`) : 조회 종료일, YYYYMMDD (KST)
        """
        return self.call('GET', '/billing/bizmoney/cost', params=self._get_params(params))

    def charge(self, params={}):
        """파라미터로 전달한 기간의 Bizmoney 충전 내역을 반환한다.

        :param params: 충전 내역 데이터를 받아오기 위한 매개변수,  search_start_dt, search_end_dt 모두 필수
        :type params: dict

        **params:**
            - *search_start_dt* (`str`) : 조회 시작일, YYYYMMDD (KST)
            - *search_end_dt* (`str`) : 조회 종료일, YYYYMMDD (KST)
        """
        return self.call('GET', '/billing/bizmoney/histories/charge', params=self._get_params(params))

    def exhaust(self, params={}):
        """파라미터로 전달한 기간의 Bizmoney 공제된 내역을 반환한다.

        :param params: 공제 내역 데이터를 받아오기 위한 매개변수,  search_start_dt, search_end_dt 모두 필수
        :type params: dict

        **params:**
            - *search_start_dt* (`str`) : 조회 시작일, YYYYMMDD (KST)
            - *search_end_dt* (`str`) : 조회 종료일, YYYYMMDD (KST)
        """
        return self.call('GET', '/billing/bizmoney/histories/exhaust', params=self._get_params(params))

    def period(self, params={}):
        """파라미터로 전달한 기간의 일자별 BizMoney 상태값을 반환한다.

        :param params: 요청한 기간동안의 데이터를 받아오기 위한 매개변수,  search_start_dt, search_end_dt 모두 필수
        :type params: dict

        **params:**
            - *search_start_dt* (`str`) : 조회 시작일, YYYYMMDD (KST)
            - *search_end_dt* (`str`) : 조회 종료일, YYYYMMDD (KST)
        """
        return self.call('GET', '/billing/bizmoney/histories/period', params=self._get_params(params))
