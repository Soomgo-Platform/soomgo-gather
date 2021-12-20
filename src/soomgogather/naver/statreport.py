from marshmallow import Schema, ValidationError, fields, validate

from ._searchad import BaseSearchAD


class StatReport(BaseSearchAD):
    """Naver SearchAd API StatReport

    Naver SearchAd API에서 발급받은 api_key, secret_key, customer_id를 사용하여 StatReport 클래스 객체를 생성한다.
    생성한 StatReport 객체로 대용량 보고서 기능을 이용하여 특정일에 발생한 대용량 보고서 다운로드(Stat 데이터)하고 광고 효과 보고서를 확인할 수 있다.

    대용량 보고서 다운로드는 계정 단위로 특정일에 발생한 광고 효과 보고서를 다운로드하는 기능으로 일 단위로만 신청 가능하며, 기간별 조회 기능은 제공되지 않는다.
    다운로드 항목에서 필요한 보고서 종류를 선택하고 생성 요청하여 사용할 수 있다.

    * 대용량 보고서의 최대 제공 기간은 최근 1년이다. 유형에 따라 기간이 상이하다.

    https://naver.github.io/searchad-apidoc/#/tags/StatReport

    사용 예시) 계정단위로 특정일에 발생한 광고 효과 보고서(Stat 리포트)를 생성하고, 등록된 모든 광고 효과 보고서를 다운로드 할 수 있다.

    .. code-block:: python

        >>> from soomgogather.naver import StatReport

        >>> stat_report = StatReport(api_key='_', secret_key='_', customer_id='_')

        >>> r = stat_report.create(params={
        ...     'report_type': 'AD_CONVERSION',
        ...     'report_date': '20211201',
        ... })

        >>> if r.status_code == 204:
        ...     print("AD_CONVERSION 광고 효과 보고서가 생성되었습니다.")

        >>> r = stat_report.list()

        >>> if r.status_code == 200:
        ...     print(r.json())

    """

    default_path = '/stat-reports'  # Stat Report에 관련된 요청을 보내기 위한 기본 uri

    class _StatReportSchema(Schema):
        report_type = fields.Str(
            attribute='reportTp',
            required=True,
        )
        report_date = fields.Str(
            attribute="statDt",
            required=True,
        )

    def _get_params(self, params):
        try:
            return self._StatReportSchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def list(self):
        """모든 등록된 보고서 작업을 검색한다."""
        return self.call('GET', self.default_path)

    def create(self, params):
        """필요한 항목을 선택하여 대용량 보고서(Stat Report)를 요청하고, 특정일에 발생한 광고 효과 보고서를 생성한다.

        https://naver.github.io/searchad-apidoc/#/operations/POST/~2Fstat-reports

        :param params: 쿼리 스트링을 구성하기 위한 매개변수
        :type params: dict

        **params:**
          - *reportTp* (`str`) : 제공되는 광고 성과 목록 (네이버에서 제공하는 항목 중에 선택)
          - *statDt* (`str`) - 특정일 (ISO 8601(UTC): 2021-12-01T00:00:00Z, YYYYMMDD(KST): 20211201)
        """

        return self.call('POST', self.default_path, params=self._get_params(params))

    def get(self, report_job_id):
        """특정 Report Job(보고서 작업)을 검색한다.

        :param report_job_id: 유효한 Report Job ID
        :type report_job_id: str
        """

        return self.call('GET', f'{self.default_path}/{report_job_id}')

    def delete_all(self):
        """모든 Report Job들을 삭제한다."""
        return self.call('DELETE', self.default_path)

    def delete(self, report_job_id):
        """해당 Report Job을 삭제한다.

        :param report_job_id: 유효한 Report Job ID
        :type report_job_id: str
        """
        return self.call('DELETE', f'{self.default_path}/{report_job_id}')
