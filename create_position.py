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
    ma.create_order(order, headers, params)


if __name__ == '__main__':
    # отложенная заявка срабатывает сразу если цена лучше чем в заявке
    create_position({'symbol': '1000PEPEUSDT', 'side': 'BUY', 'type': 'LIMIT', 'price': 0.0065600, 'quantity': 1400})
    # покупка по маркету
    # create_position({'symbol': 'BLZUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 35})
    # снимает все отложенные заявки для этой пары
    # create_position({'symbol':'BLZUSDT', 'type': 'CancelOrder'})
    # закрывает ордер по указанной цене, если позиция SELL то и STOP_MARKET в плюс SELL а в минус BUY
    # закрывает ордер по указанной цене, если позиция BUY то и STOP_MARKET в плюс BUY а в минус SELL
    # create_position({'symbol':'BLZUSDT', 'type': 'STOP_MARKET', 'stopprice': 0.357, 'side': 'BUY', 'closePosition': 'true', 'quantity': 'Close-All'})
    # увеличивает позицию отложкой по целевой цене если дано quantity, closePosition не равно true
    # create_position({'symbol': '1000PEPEUSDT', 'type': 'STOP_MARKET', 'side': 'SELL', 'stopprice': 0.0068600, 'quantity': 1400})
    # проверка аккаунта
    # create_position({'acc': 'acc'})
    # print(query_new_prices())
