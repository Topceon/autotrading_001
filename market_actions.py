import time

import requests

import keys
import action_decition as ad

BASE_URL = "https://fapi.binance.com"
klines_url_order = "/fapi/v1/klines"
url_order = "/fapi/v1/order"
listen_key = '/fapi/v1/listenKey'


def get_timestamp():
    return str(int(time.time() * 1000))


def query_new_prices() -> dict:
    resp = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    a = resp.json()
    d = {i['symbol']: float(i['price']) for i in a if i['symbol'][-4:] == 'USDT'}
    return d


def get_klines(coin):
    params = {
        'symbol': coin,
        'interval': '1m',
        'limit': 499
    }
    headers = {'X-MBX-APIKEY': keys.API_key}
    req = requests.get(BASE_URL + klines_url_order, headers=headers, params=params)
    klines = req.json()
    return klines


def new_listen_key(headers, params):
    req = requests.post(BASE_URL + listen_key, headers=headers, params=params)
    return req.json()


def create_order(order, headers, params):
    req = requests.post(BASE_URL + url_order, headers=headers, params=params)
    return req.json()

def del_orders(headers, params):
    req = requests.delete(BASE_URL + "/fapi/v1/allOpenOrders", headers=headers, params=params)
    return req.json()

def del_order(headers, params):
    req = requests.delete(BASE_URL + "/fapi/v1/order", headers=headers, params=params)
    return req.json()

def get_acc_info(order, headers, params):
    req = requests.get(BASE_URL + "/fapi/v1/openOrders", headers=headers, params=params)
    return req.json()


def get_acc_balace(headers, params):
    req = requests.get(BASE_URL + "/fapi/v2/account", headers=headers, params=params)
    balance_info = req.json()
    time.sleep(3)
    return balance_info

def get_precisions():
    price_precision = {}
    lot_size = {}
    req = requests.get(BASE_URL + '/fapi/v1/exchangeInfo')
    info = req.json()
    for i in info['symbols']:
        s = i['symbol']
        price_precision[s] = ad.lot_size_precision(i['filters'][0]['tickSize'])
        lot_size[s] = float(i['filters'][1]['stepSize'])
    return price_precision, lot_size


if __name__ == '__main__':
    # входящие данные ["BLZUSDT", "AVAXUSDT", "ARBUSDT"]
    # результат {"AVAXUSDT":[время открытия свечи, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем]}
    a, b = get_precisions()
    print(a)
    print(b)
    # print(get_acc_info())
