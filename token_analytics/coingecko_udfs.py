import string
from tokenize import String
from numpy import NAN
import xlwings as xw
import requests as req
import ratelimit
import pandas as pd
import matplotlib.pyplot as plt


class Simple_Coingecko_Api:
    def __init__(self):
        self.default_header = {
            "accept": "application/json"
        }

    def get_json(self, uri, params=None):
        if params is None:
            res = req.get(url=f'https://api.coingecko.com/api/v3/{uri}', headers = self.default_header)
        else:
            res = req.get(url=f'https://api.coingecko.com/api/v3/{uri}', headers = self.default_header, params=params)
        if res.status_code != 200:
            return None
        return res.json()

coingecko_api = Simple_Coingecko_Api()

@xw.func
@xw.ret(index=False, header=True, expand='table')
def coingecko_get_category_list():
    data = coingecko_api.get_json('/coins/categories/list')
    if data is None:
        return None
    return pd.DataFrame(data)


@xw.func
@xw.ret(index=False, header=True, expand='table')
def coingecko_get_coins_list():
    data = coingecko_api.get_json('/coins/list')
    if data is None:
        return None
    return pd.DataFrame(data)

@xw.func
@xw.ret(index=False, header=True, expand='table')
def coingecko_get_coins_list_by_category(category):
    print(category)
    params = {
        "vs_currency": 'usd',
        "category": category,
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
    }
    data = coingecko_api.get_json('/coins/markets', params=params)
    if data is None:
        return None
    return pd.DataFrame(data)

# @xw.func
# @xw.ret(index=False, header=True, expand='table')
# def coingecko_search_coin_id(symbol):
#     data = coingecko_api.get_json('/coins/list')
#     if data is None:
#         return None
#     return pd.DataFrame(data)

@xw.func
def gecko_get_price(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['current_price']['usd']

@xw.func
def gecko_get_ath(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['ath']['usd']

@xw.func
def gecko_get_ath_date(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['ath_date']['usd']

@xw.func
def gecko_get_atl(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['atl']['usd']

@xw.func
def gecko_get_atl_date(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['atl_date']['usd']

@xw.func
def gecko_get_marketcap(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['market_cap']['usd']

@xw.func
def gecko_get_fdv(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['fully_diluted_valuation']['usd']

@xw.func
def gecko_get_marketcap_rank(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['market_cap_rank']

@xw.func
def gecko_get_total_volume(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['total_volume']['usd']

@xw.func
def gecko_get_total_supply(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['total_supply']

@xw.func
def gecko_get_circulating_supply(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['circulating_supply']

@xw.func
def gecko_get_max_supply(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['max_supply']

@xw.func
def gecko_get_price_change_percentage_24h(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['price_change_percentage_24h']/100

@xw.func
def gecko_get_price_change_percentage_7d(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['price_change_percentage_7d']/100

@xw.func
def gecko_get_price_change_percentage_30d(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['price_change_percentage_30d']/100


@xw.func
def gecko_get_price_change_percentage_1y(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['market_data']['price_change_percentage_1y']/100

@xw.func
def gecko_get_symbol(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['symbol']

@xw.func
def gecko_get_name(id):
    data = coingecko_api.get_json(f'/coins/{id}')
    if data is None:
        return None
    return data['name']

