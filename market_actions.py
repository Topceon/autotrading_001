import time
import requests

import keys

BASE_URL = "https://fapi.binance.com"
klines_url_order = "/fapi/v1/klines"
url_order = "/fapi/v1/order"


def get_timestamp():
    return str(int(time.time() * 1000))


def get_deposit_size():
    """Запрашиваем размер депозита на бирже
    размер должен быть в долларовом эквиваленте"""
    # TODO исправить захардкоженный вариант после отработки работоспособности других функций
    return 10


def query_new_prices() -> dict:
    resp = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    a = resp.json()
    d = {i['symbol']: float(i['price']) for i in a if i['symbol'][-4:] == 'USDT'}
    return d


def get_klines(coin):
    params = {
        'symbol': coin,
        'interval': '1m',
        'limit': 50
    }
    headers = {'X-MBX-APIKEY': keys.API_key}
    req = requests.get(BASE_URL + klines_url_order, headers=headers, params=params)
    klines = req.json()
    return klines


def create_order(order, headers, params):
    if order['type'] == 'CancelOrder':
        req = requests.delete(BASE_URL + "/fapi/v1/allOpenOrders", headers=headers, params=params)
    else:
        req = requests.post(BASE_URL + url_order, headers=headers, params=params)
    print(req.json())


if __name__ == '__main__':
    # входящие данные ["BLZUSDT", "AVAXUSDT", "ARBUSDT"]
    # результат {"AVAXUSDT":[время открытия свечи, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем]}
    print(get_klines("1000PEPEUSDT"))
