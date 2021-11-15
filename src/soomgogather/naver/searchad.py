from soomgogather.naver.request import RequestSearchAd

class Bizmoney:

    def __init__(self, api_key, secret_key, customer_id, report_type):
        self.base_url = 'https://api.naver.com'
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id
        self.report_type = report_type
        
        # API request class
        self.req = RequestSearchAd(self.base_url, self.api_key, self.secret_key, self.customer_id)
    

    def get_report_info(self, report_job_id):
        uri = '/billing/bizmoney/' + str(report_job_id)

        print("request bizmoney info")

        # get report info
        r = self.req.request_get(uri)
        print(f'bizmoney info response status_code = {r.status_code}')  # success: 200

        print(f'response body\n{r.json()}')
        return r


    def get_report_list(self):
        return ''


    def create_report(self):
        return ''


    def delete_report(self):
        return ''

