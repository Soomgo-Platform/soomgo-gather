from marshmallow import Schema, ValidationError, fields

from ._searchad import BaseSearchAD


class Bizmoney(BaseSearchAD):
    class _BizmoneySchema(Schema):
        search_start_dt = fields.Str(attribute='searchStartDt', required=True)
        search_end_dt = fields.Str(attribute='searchEndDt', required=True)
        stat_dt = fields.Str(attribute='statDt')

    def set_params(self, params):
        try:
            return self._BizmoneySchema().load(params)
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
