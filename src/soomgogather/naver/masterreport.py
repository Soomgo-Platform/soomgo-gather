from marshmallow import Schema, ValidationError, fields, validate

from ._searchad import BaseSearchAD


class MasterReport(BaseSearchAD):
    """Naver SearchAd API MasterReport

    Naver SearchAd API에서 발급받은 api_key, secret_key, customer_id를 사용하여 MasterReport 클래스 객체를 생성한다.
    생성한 MasterReport 객체로 마스터 기능을 이용하여 종류별 광고 정보 일괄 다운로드(마스터 데이터)하고 각 광고 정보를 확인할 수 있다.

    광고 정보 일괄 다운로드는 특정 시점을 기준으로 광고 계정에 등록된 모든 광고 정보를 다운로드하는 기능으로 상시로 변경되는 정보는 제공되지 않으며 사용자가 등록한 광고 정보만 제공된다.
    다운로드된 광고 정보는 각각 종류별 정보만 담고있다.

    * 광고 정보 일괄 다운로드(마스터 기능 이용하기)의 최대 제공 기간은 '최근 2년(730일)'이다.
    * 데이터가 존재하지 않는 경우 다운로드 링크는 제공되지 않는다.
    * 일부 항목은 변경 분 데이터를 제공하지 않는다.
    * 릴리즈 노트 참고 - (http://naver.github.io/searchad-apidoc/#/release-notes)

    https://naver.github.io/searchad-apidoc/#/tags/MasterReport

    사용 예시) 특정 시점을 기준으로 광고 계정에 광고 정보에 대한 마스터리포트를 생성하고, 등록된 모든 광고 정보를 다운로드 할 수 있다.

    .. code-block:: python

        >>> from soomgogather.naver import MasterReport

        >>> master_report = MasterReport(api_key='_', secret_key='_', customer_id='_')

        >>> r = master_report.create(params={
        ...     'item': 'Media',
        ... })

        >>> if r.status_code == 204:
        ...     print("Media 광고 정보가 생성되었습니다.")

        >>> r = master_report.list()

        >>> if r.status_code == 200:
        ...     print(r.json())

    """

    default_path = '/master-reports'  # Master Report에 관련된 요청을 보내기 위한 기본 uri

    class _MasterReportSchema(Schema):
        item = fields.Str(
            attribute='item',
            required=True,
        )

        from_time = fields.Str(attribute="fromTime")

    def _get_params(self, params):
        try:
            return self._MasterReportSchema().load(params)
        except ValidationError as err:
            raise ValueError(f"incorrect parameters: {err}")

    def list(self):
        """요청을 통해 생성된 광고 정보에 대한 작업 목록(최대 100개)을 가져온다."""
        return self.call('GET', self.default_path)

    def create(self, params):
        """필요한 항목을 선택하여 마스터 리포트를 요청하고, 해당 항목에 대한 광고 정보 리포트를 생성한다.

        https://gist.github.com/naver-searchad/186ca42e1e8596b0e3dcf74e3a86c04f

        :param params: 쿼리 스트링을 구성하기 위한 매개변수, item은 필수
        :type params: dict

        **params:**
          - *item* (`str`) : 제공되는 광고 정보 목록 (네이버에서 제공하는 항목 중에 선택)
          - *from_time* (`str, optional`) - 특정 시점 (ISO 8601 UTC, 2021-12-01T00:00:00Z)

        """

        return self.call('POST', self.default_path, params=self._get_params(params))

    def get(self, job_id):
        """특정 job_id를 사용해서 해당 마스터 리포트의 작업 상세 정보를 가져온다.

        :param job_id: 유효한 마스터 리포트 Job id
        :type job_id: str
        """

        return self.call('GET', f'{self.default_path}/{job_id}')

    def delete_all(self):
        """모든 마스터 리포트 작업을 삭제한다."""
        return self.call('DELETE', self.default_path)

    def delete(self, job_id):
        """해당 마스터 리포트를 job id로 삭제한다.

        :param job_id: 유효한 마스터 리포트 Job id
        :type job_id: str
        """
        return self.call('DELETE', f'{self.default_path}/{job_id}')
