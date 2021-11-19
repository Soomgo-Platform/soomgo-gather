from marshmallow import Schema, fields
from ._searchad import BaseSearchAD


class Bizmoney(BaseSearchAD):
    def status(self):
        return self.call('GET', '/billing/bizmoney')

    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(data_key='searchStartDt', required=True)
        search_end_dt = fields.Str(data_key='searchEndDt', required=True)

    def cost(self, params={}):
        return self.call('GET', '/billing/bizmoney/cost', params=self._BizmoneySchema().dump(params))

    def charge(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/charge', params=self._BizmoneySchema().dump(params))

    def exhaust(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/exhaust', params=self._BizmoneySchema().dump(params))

    def period(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/period', params=self._BizmoneySchema().dump(params))
