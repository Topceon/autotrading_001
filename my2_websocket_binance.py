import websocket
import requests
import threading
import time
import json

import keys
import main_app as rv
import market_actions as ma
import strategy_2 as s2

COIN_PAIRS = ['1000PEPEUSDT', 'WLDUSDT']
BALANCER = {COIN: 0 for COIN in COIN_PAIRS}
BAND_SIZE = [1, 5, 10]


class Variant:
    def __init__(self, coin_pair, band_size):
        self.balancer = 0
        self.coin_pair = coin_pair
        self.band_size = band_size
        self.max_position = 0
        self.min_position = 0
        self.id_positions = []

    def create_positions(self):  # создает первые две позиции на расстоянии 5 процентов от цены при первом запуске
        if self.balancer <= 0:
            s2.create_position(self.coin_pair, self.max_position, 1)
        if self.balancer >= 0:
            s2.create_position(self.coin_pair, self.min_position, -1)

    def recreate_positions(self):  # при срабатывании верхней лимитки выставляется нижняя и наоборот
        pass

    def moving_band(self):  # двигает цены лимиток на 5 процентов от пиковых значений за последнее время
        pass

    def klines(self, kline):  # достает последнюю свечу с биржи
        print(kline)


all_vars = []

for i in COIN_PAIRS:
    for j in BAND_SIZE:
        j = Variant(i, j)
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
        prices[coin] = ma.get_klines(coin)
    for j in all_vars:
        j.klines(prices[j.coin_pair])
        j.create_positions()


def message_handler(_, message):
    global BALANCER
    data_2 = json.JSONDecoder().decode(message)
    # print(data_2)
    if data_2['e'] and data_2['e'] == 'ORDER_TRADE_UPDATE':
        print(data_2['o']['x'])
        if data_2['o']['x'] == 'TRADE':
            if data_2['o']['S'] == 'BUY':
                BALANCER[data_2['o']['s']] = -1
            else:
                BALANCER[data_2['o']['s']] = 1
    print(BALANCER)


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
    options_for_functions(begin_all_vars, 60, [COIN_PAIRS, BALANCER])


functions_for_start = [start_ws,
                       renew_listen_key,
                       start_all_vars
                       ]

# threads = [threading.Thread(target=i, daemon=True) for i in functions_for_start]
# for e in threads:
#     e.start()
# for e in threads:
#     e.join()

if __name__ == '__main__':
    begin_all_vars()
