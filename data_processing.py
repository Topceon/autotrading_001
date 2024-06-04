import websocket
import requests
import threading
import time
import json

import keys
import market_actions as ma
import create_position as cp

DIAPASON = [1, 3, 0.1]  # [конечный процент, начальный процент, разница между ставками]
COIN_PAIRS = ['1000PEPEUSDT', 'WLDUSDT']
PRICE_PRECISION = {'1000PEPEUSDT': 7, 'WLDUSDT': 4}
LOT_SIZE = {'1000PEPEUSDT': 1, 'WLDUSDT': 1}
BALANCE_PESETAGE = 10
BALANCE = 10
DEEP_ORDERS = 3

BAND_SIZE = list(reversed([i / 10 for i in range(DIAPASON[0] * 10, DIAPASON[1] * 10 + 1, int(DIAPASON[2] * 10))]))


def create_position(coin, price):
    str_precision = str(LOT_SIZE[coin]).count('0')
    quantity = round(int(10 / price) + LOT_SIZE[coin], str_precision)
    order = cp.create_position({'symbol': '1000PEPEUSDT',
                                'side': "BUY",
                                'type': 'LIMIT',
                                'price': round(price, PRICE_PRECISION[coin]),
                                'quantity': quantity})
    return order #['orderId']


dict_1 = ''
def foo():
    global dict_1
    try:
        dict_1 = create_position('1000PEPEUSDT', 0.0120000)
    except Exception as e:
        time.sleep(1)
        print(e)
        foo()

if __name__ == '__main__':
    foo()
    print(dict_1)
