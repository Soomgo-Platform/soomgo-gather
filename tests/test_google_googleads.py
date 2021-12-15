
from soomgogather.google import GoogleAds
import pandas as pd

customer_id = "123456"

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

def _create_client_from_file():

    service = GoogleAds(key_file='api_google_googleads.yaml')

    return service

def _create_client_from_dict():

    credentials_dict = {
        'developer_token': 'developer_token',
        'refresh_token': 'refresh_token',
        'client_id': '434sdfx-123zdfserw.apps.googleusercontent.com',
        'client_secret': 'GSDE4R-ADCSER',
        'use_proto_plus': True,
        'login_customer_id': "5422345",
        }

    service = GoogleAds(dict=credentials_dict)

    return service

def _create_client_from_default():

    service = GoogleAds()

    return service

def test_googleads_stream_file():
    service = _create_client_from_file()
    stream = service.search_stream_request(params)
    
    for batch in stream:
        for row in batch.results:
            campaign = row.campaign
            ad_group = row.ad_group
            criterion = row.ad_group_criterion
            print(
                f'CampaignId" {campaign.id}"  '
                f'AdGroupId" {ad_group.id}" '
                f'CriterionId" {criterion.criterion_id}" '
                f'Status" {criterion.status}" '
                f'CpcBid" {ad_group.cpc_bid_micros}" '
                f'CpmBid" {ad_group.cpm_bid_micros}" '
                f'CpvBid" {ad_group.cpv_bid_micros}" '
                f'FinalUrls" {criterion.final_urls}" '
            )
    assert stream

def test_googleads_stream_dict():

    service = _create_client_from_dict()
    stream = service.search_stream_request(params)
    # _print_data(stream)
    assert stream

def test_googleads_stream_default():
    import os
    os.environ["GOOGLE_ADS_CONFIGURATION_FILE_PATH"] = "/Users/rosa/Downloads/api_google_googleads (2).yaml"

    service = _create_client_from_default()
    try:
        stream = service.search_stream_request(params)
    except Exception as err:
        assert type(err) == ValueError

