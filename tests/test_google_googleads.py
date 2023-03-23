from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.v13.enums.types.summary_row_setting import SummaryRowSettingEnum
from google.ads.googleads.v13.services.services.google_ads_service.client import GoogleAdsServiceClient
from google.ads.googleads.v13.services.types.google_ads_service import SearchGoogleAdsStreamRequest

from soomgogather.google import GoogleAds

customer_id = "1231231"

query = """
  SELECT
    campaign.id,
    ad_group.id,
    ad_group_criterion.criterion_id,
    ad_group_criterion.age_range.type,
    ad_group_criterion.status,
    ad_group.cpc_bid_micros,
    ad_group.cpm_bid_micros,
    ad_group.cpv_bid_micros,
    ad_group_criterion.final_urls,
    ad_group_criterion.final_url_suffix,
    metrics.average_cost
  FROM keyword_view
  WHERE ad_group_criterion.status in ('ENABLED', 'PAUSED') and segments.date DURING YESTERDAY
  LIMIT 5
"""

params = {
    'query': query,
    'customer_id': customer_id,
}


def _create_client_from_file(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.load_from_storage', return_value=GoogleAdsClient)
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_service', return_value=GoogleAdsServiceClient)

    credentials_dict = {'key_file': 'api_google_googleads.yaml'}

    service = GoogleAds(credentials=credentials_dict)

    return service


def _create_client_from_dict(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.load_from_dict', return_value=GoogleAdsClient)
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_service', return_value=GoogleAdsServiceClient)

    credentials_dict = {
        'developer_token': 'AEARD234sd3w_Es2',
        'refresh_token': 'SD32rssdf42-AsdF435sf-VSSD3sfxv',
        'client_id': '134463443-4SFxfwdxx.apps.googleusercontent.com',
        'client_secret': 'HESDFES8-SNsdfSEF',
        'use_proto_plus': True,
        'login_customer_id': "2352373",
    }

    service = GoogleAds(credentials=credentials_dict)
    return service


def _create_client_from_default(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.load_from_storage', return_value=GoogleAdsClient)
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_service', return_value=GoogleAdsServiceClient)

    service = GoogleAds()

    return service


def test_googleads_stream_file(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_type', return_value=SearchGoogleAdsStreamRequest)
    mocker.patch(
        'google.ads.googleads.v13.services.services.google_ads_service.client.GoogleAdsServiceClient.search_stream',
        return_value='success',
    )
    service = _create_client_from_file(mocker)
    stream = service.search_stream_request(params)

    assert stream


def test_googleads_stream_dict(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_type', return_value=SearchGoogleAdsStreamRequest)
    mocker.patch(
        'google.ads.googleads.v13.services.services.google_ads_service.client.GoogleAdsServiceClient.search_stream',
        return_value='success',
    )

    params = {
        'query': query,
        'customer_id': customer_id,
        'summary_row_setting': 'UNSPECIFIED',
    }

    service = _create_client_from_dict(mocker)

    try:
        service.search_stream_request(params)
    except Exception as err:
        assert type(err) == AttributeError

    params = {
        'query': query,
        'customer_id': customer_id,
        'summary_row_setting': {'row_setting': 'SUMMARY_ROW_ONLY'},
    }

    service = _create_client_from_dict(mocker)

    try:
        service.search_stream_request(params)
    except Exception as err:
        assert type(err) == ValueError


def test_googleads_stream_default(mocker):
    mocker.patch('google.ads.googleads.client.GoogleAdsClient.get_type', return_value=SearchGoogleAdsStreamRequest)
    mocker.patch(
        'google.ads.googleads.v13.services.services.google_ads_service.client.GoogleAdsServiceClient.search_stream',
        return_value='success',
    )

    import os

    os.environ["GOOGLE_ADS_CONFIGURATION_FILE_PATH"] = "api_google_googleads.yaml"

    params = {
        'query': query,
        'customer_id': customer_id,
        'summary_row_setting': 'UNSPECIFIED!',
    }

    service = _create_client_from_default(mocker)
    try:
        service.search_stream_request(params)
    except Exception as err:
        assert type(err) == ValueError
