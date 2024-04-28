import hashlib
import hmac

import market_actions as ma
import keys

BASE_URL = "https://fapi.binance.com"
url_order = "/fapi/v1/order"


def signature(params):
    query_string = '&'.join([f'{key}={params[key]}' for key in params])
    signature = hmac.new(keys.Secret_key.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
    return signature


def create_position(order):
    global url_order
    if order["type"] == "LIMIT":
        params = {
            'symbol': order['symbol'],
            'type': order['type'],
            'side': order['side'],
            'timestamp': ma.get_timestamp(),
            'quantity': order['quantity'],
            'price': order['price'],
            'timeInForce': 'GTC'
        }

    if order['type'] == 'MARKET':
        params = {
            'symbol': order['symbol'],
            'type': order['type'],
            'side': order['side'],
            'timestamp': ma.get_timestamp(),
            'quantity': order['quantity']
        }

    if order['type'] == 'STOP_MARKET':
        params = {
            'symbol': order['symbol'],
            'timestamp': ma.get_timestamp(),
            'type': order['type'],
            'side': order['side'],
            'stopprice': order['stopprice'],
            'quantity': order['quantity'],
            'closePosition': 'false'
        }

    if order['type'] == 'CancelOrder':
        params = {
            'symbol': order['symbol'],
            'timestamp': ma.get_timestamp()
        }

    params['signature'] = signature(params)
    headers = {'X-MBX-APIKEY': keys.API_key}
    if order['type'] == 'CancelOrder':
        return ma.del_orders(headers, params)
    return ma.create_order(order, headers, params)


def new_listen_key():
    params = {
        'timestamp': ma.get_timestamp()
    }
    params['signature'] = signature(params)
    headers = {'X-MBX-APIKEY': keys.API_key}
    return ma.new_listen_key(headers, params)


def close_order_with_id(order_id):
    pass


def get_acc_info(order):
    params = {
        'symbol': order['symbol'],
        'timestamp': ma.get_timestamp()
    }

    params['signature'] = signature(params)
    headers = {'X-MBX-APIKEY': keys.API_key}
    return ma.get_acc_info(order, headers, params)


def get_unrealized_profit():
    params = {
        'timestamp': ma.get_timestamp()
    }

    params['signature'] = signature(params)
    headers = {'X-MBX-APIKEY': keys.API_key}

    for i in get_acc_balace()['positions']:
        if i['unrealizedProfit'] != '0.00000000':
            print(i['symbol'], i['unrealizedProfit'])
    return ma.get_acc_balace(headers, params)


def get_acc_balace():
    params = {
        'timestamp': ma.get_timestamp()
    }

    params['signature'] = signature(params)
    headers = {'X-MBX-APIKEY': keys.API_key}
    all_info = ma.get_acc_balace(headers, params)
    for i in all_info['assets']:
        if i['asset'] == 'USDT':
            return i['walletBalance']


if __name__ == '__main__':
    # отложенная заявка срабатывает сразу если цена лучше чем в заявке
    # print(create_position({'symbol': '1000PEPEUSDT', 'side': 'BUY', 'type': 'LIMIT', 'price': 0.0073600, 'quantity': 1400}))

    # покупка по маркету
    # create_position({'symbol': 'BLZUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 35})

    # снимает все отложенные заявки для этой пары
    # print(create_position({'symbol':'1000PEPEUSDT', 'type': 'CancelOrder'}))

    # закрывает ордер по указанной цене, если позиция SELL то и STOP_MARKET в плюс SELL а в минус BUY
    # закрывает ордер по указанной цене, если позиция BUY то и STOP_MARKET в плюс BUY а в минус SELL
    # print(create_position({'symbol': '1000PEPEUSDT', 'type': 'STOP_MARKET', 'stopprice': 0.357, 'side': 'BUY', 'closePosition': 'true', 'quantity': 'Close-All'}))

    # увеличивает позицию отложкой по целевой цене если дано quantity, closePosition не равно true
    # print(create_position({'symbol': '1000PEPEUSDT', 'type': 'STOP_MARKET', 'side': 'BUY', 'stopprice': 0.0078000, 'quantity': 1400}))

    # проверка аккаунта
    # create_position({'acc': 'acc'})
    # print(query_new_prices())

    # получить новый listen_key, нужен для websocket
    # print(new_listen_key())

    print(get_acc_balace())
    print("")
