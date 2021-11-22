from marshmallow import Schema, fields, ValidationError
from ._searchad import BaseSearchAD


class Bizmoney(BaseSearchAD):

    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(data_key='searchStartDt', required=True)
        search_end_dt = fields.Str(data_key='searchEndDt', required=True)
        stat_dt = fields.Str(data_key='statDt')
    
    def set_params(self,params):
        try:
            request_params = self._BizmoneySchema().dump(params)
            self._BizmoneySchema().load(request_params)
            return request_params
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def status(self):
        return self.call('GET', '/billing/bizmoney')

    def cost(self, params={}):
        return self.call('GET', '/billing/bizmoney/cost', params=self.set_params(params))

    def charge(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/charge', params=self.set_params(params))

    def exhaust(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/exhaust', params=self.set_params(params))

    def period(self, params={}):
        return self.call('GET', '/billing/bizmoney/histories/period', params=self.set_params(params))
