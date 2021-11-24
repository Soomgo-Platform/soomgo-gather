from marshmallow import Schema, ValidationError, fields

from ._searchad import BaseSearchAD


class Bizmoney(BaseSearchAD):
    """이 클래스의 동작 요약.

    이 클래스의 동작 설명

    .. code-block:: python

        from soomgogather.naver import Bizmoney

        bizmoney = Bizmoney(api_key='_', secret_key='_', customer_id='_')

        bizmoney.cost(params={
            'search_start_dt': '20211118',
            'search_end_dt': '20211118',
        }).status_code == 200

    """
    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(attribute='searchStartDt', required=True)
        search_end_dt = fields.Str(attribute='searchEndDt', required=True)
        stat_dt = fields.Str(attribute='statDt')

    def get_params(self, params):
        """메소드 동작 요약"""
        try:
            return self._BizmoneySchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")


    def status(self):
        """메소드 동작 요약"""
        return self.call('GET', '/billing/bizmoney')

    def cost(self, params={}):
        """메소드 동작 요약"""
        return self.call('GET', '/billing/bizmoney/cost', params=self.get_params(params))

    def charge(self, params={}):
        """메소드 동작 요약"""
        return self.call('GET', '/billing/bizmoney/histories/charge', params=self.get_params(params))

    def exhaust(self, params={}):
        """메소드 동작 요약"""
        return self.call('GET', '/billing/bizmoney/histories/exhaust', params=self.get_params(params))

    def period(self, params={}):
        """메소드 동작 요약"""
        return self.call('GET', '/billing/bizmoney/histories/period', params=self.get_params(params))
