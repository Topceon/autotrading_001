import websocket
import requests
import threading
import time
import json

import keys
import market_actions as ma
import create_position as cp

COIN_PAIRS = ['1000PEPEUSDT', 'WLDUSDT']
BAND_SIZE = [1, 3, 5]
PRICE_PRECISION = {'1000PEPEUSDT': 7, 'WLDUSDT': 4}
LOT_SIZE = {'1000PEPEUSDT': 1, 'WLDUSDT': 1}


class Variant:
    def __init__(self, coin_pair, band_size, prise_precision, lot_size):
        self.balancer = 0
        self.coin_pair = coin_pair
        self.band_size = band_size
        self.sell_position = 99999999
        self.buy_position = 0
        self.id_positions = []
        self.lot_size = lot_size
        self.prise_precision = prise_precision
        self.lot_size_precision = self.lot_size_precision()

    def lot_size_precision(self):
        str_precision = str(self.lot_size)
        return str_precision.count('0')

    def create_positions(self):  # создает две позиции на расстоянии band_size процентов от цены
        for i in self.id_positions:
            cp.close_order_with_id(self.coin_pair, i)
        self.id_positions = []
        if self.balancer <= 0:
            quantity = round(int(10 / self.sell_position) + self.lot_size, self.lot_size_precision)
            order = cp.create_position({'symbol': self.coin_pair,
                                        'side': 'SELL',
                                        'type': 'LIMIT',
                                        'price': self.sell_position,
                                        'quantity': quantity})
            self.id_positions.append(order['orderId'])
        if self.balancer >= 0:
            quantity = round(int(10 / self.sell_position) + self.lot_size, self.lot_size_precision)
            order = cp.create_position({'symbol': self.coin_pair,
                                        'side': 'BUY',
                                        'type': 'LIMIT',
                                        'price': self.buy_position,
                                        'quantity': quantity})
            self.id_positions.append(order['orderId'])
        print(self.id_positions, self.balancer)

    def klines(self, kline):  # [время открытия, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем]
        if self.sell_position > float(kline[4]) * ((100 + self.band_size) / 100):  # цена минимума свечи [4]
            self.sell_position = float(kline[4]) * ((100 + self.band_size) / 100)
            self.sell_position = round(self.sell_position, self.prise_precision)
        if self.buy_position < float(kline[2]) * ((100 - self.band_size) / 100):  # цена максимума свечи [2]
            self.buy_position = float(kline[2]) * ((100 - self.band_size) / 100)
            self.buy_position = round(self.buy_position, self.prise_precision)

    def change_balanser(self, order):  # при срабатывании верхней лимитки выставляется нижняя и наоборот
        if order == 'BUY':
            self.balancer = -1
        else:
            self.balancer = 1
        print(self.balancer)
        self.create_positions()



all_vars = []

for i in COIN_PAIRS:
    for j in BAND_SIZE:
        j = Variant(i, j, PRICE_PRECISION[i], LOT_SIZE[i])
        all_vars.append(j)


def options_for_functions(foo, sec, args, after=True):
    while True:
        if after:
            foo(*args)
            time.sleep(sec)
        else:
            time.sleep(sec)
            foo(*args)


def begin_all_vars():
    prices = {}
    for coin in COIN_PAIRS:
        cp.create_position({'symbol': coin, 'type': 'CancelOrder'})
        prices[coin] = ma.get_klines(coin)[-1]
    for j in all_vars:
        j.klines(prices[j.coin_pair])
        # j.create_positions()


def message_handler(_, message):
    data_2 = json.JSONDecoder().decode(message)
    # print(data_2)
    if data_2['e'] and data_2['e'] == 'ORDER_TRADE_UPDATE':
        print(data_2['o']['i'])
        if data_2['o']['x'] == 'TRADE':
            for i in all_vars:
                print(data_2['o']['i'], i.id_positions, data_2['o']['S'])
                if data_2['o']['i'] in i.id_positions:
                    i.change_balanser(data_2['o']['S'])
                    print('соответствуют')


listen_key = ''


def new_listen_key():
    global listen_key
    headers = {'X-MBX-APIKEY': keys.API_key}
    try:
        listen_key = requests.post('https://fapi.binance.com/fapi/v1/listenKey',
                                   headers=headers)
        print(listen_key.json())
    except Exception as e:
        print('Проблема ключа', e)
        time.sleep(10)
        new_listen_key()


new_listen_key()


def start_ws():
    while True:
        try:
            ws = websocket.WebSocketApp('wss://fstream.binance.com/ws/' + listen_key.json()['listenKey'],
                                        on_message=message_handler)
            ws.run_forever()
            print('Test')
            time.sleep(5)
        except Exception as e:
            print('Проблема сокета', e)
            time.sleep(5)


def renew_listen_key():
    options_for_functions(new_listen_key, 3500, [], after=False)


def start_all_vars():
    options_for_functions(begin_all_vars, 60, [])


functions_for_start = [start_ws,
                       start_all_vars,
                       renew_listen_key
                       ]

threads = [threading.Thread(target=i, daemon=True) for i in functions_for_start]
for e in threads:
    e.start()
for e in threads:
    e.join()

if __name__ == '__main__':
    pass
    # begin_all_vars()
