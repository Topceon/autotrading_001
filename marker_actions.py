import time
import requests
import hashlib
import hmac

import keys

BASE_URL = "https://fapi.binance.com"
url_order = "/fapi/v1/order"


def create_query_string(params):
    query_string = '&'.join([f'{key}={params[key]}' for key in params])
    signature = hmac.new(keys.Secret_key.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
    params['signature'] = signature
    headers = {'X-MBX-APIKEY': keys.API_key}

    if params['type'] == 'CancelOrder':
        req = requests.delete(BASE_URL + url_order, headers=headers, params=params)
    else:
        req = requests.post(BASE_URL + url_order, headers=headers, params=params)
    print(req.json())


def get_timestamp():
    return str(int(time.time() * 1000))


def query_new_prices() -> dict:
    resp = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    a = resp.json()
    d = {i['symbol']: float(i['price']) for i in a if i['symbol'][-4:] != 'BUSD'}
    return d


def limit_pos(order):
    params = {
        'symbol': order['symbol'],
        'type': order['type'],
        'side': order['side'],
        'timestamp': get_timestamp(),
        'quantity': order['quantity'],
        'price': order['price'],
        'timeInForce': 'GTC'
    }
    create_query_string(params)


def market_pos(order):
    params = {
        'symbol': order['symbol'],
        'type': order['type'],
        'side': order['side'],
        'timestamp': get_timestamp(),
        'quantity': order['quantity']
    }
    create_query_string(params)


def stop_market(order):
    params = {
        'symbol': order['symbol'],
        'timestamp': get_timestamp(),
        'type': order['type'],
        'side': order['side'],
        'stopprice': order['stopprice'],
        'quantity': 35,
        'closePosition': 'false'
    }
    create_query_string(params)


def cancel_order(order):
    params = {
        'symbol': order['symbol'],
        'timestamp': get_timestamp()
    }
    create_query_string(params)


if __name__ == '__main__':
    pass
