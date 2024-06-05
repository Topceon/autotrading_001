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
DEEP_ORDERS = 4

BAND_SIZE = list(
    reversed([i / 10 for i in range(int(DIAPASON[0] * 10), int(DIAPASON[1] * 10 + 1), int(DIAPASON[2] * 10))]))


def close_order_with_id(coin, order_id):
    try:
        cp.close_order_with_id(coin, order_id)
    except Exception as e:
        print("Не получилось удалить ставку", e)
        time.sleep(10)
        close_order_with_id(coin, order_id)


class Variant:
    def __init__(self, coin_pair, prise_precision, lot_size):
        self.balancer = [0 for _ in BAND_SIZE]
        self.coin_pair = coin_pair
        self.band_size = BAND_SIZE
        self.id_sell_positions = [None for _ in BAND_SIZE]
        self.id_buy_positions = [None for _ in BAND_SIZE]
        self.sell_prices = [99999999 for _ in BAND_SIZE]
        self.buy_prices = [0 for _ in BAND_SIZE]
        self.lot_size = lot_size
        self.prise_precision = prise_precision
        self.lot_size_precision = self.lot_size_precision()
        self.rebalanser = 0

    def lot_size_precision(self):
        str_precision = str(self.lot_size)
        return str_precision.count('0')

    def create_position(self, price, side, index):
        quantity = round(int(BALANCE / BALANCE_PESETAGE / price) + self.lot_size, self.lot_size_precision)
        try:
            if side == "BUY":
                order = cp.create_position({'symbol': self.coin_pair,
                                            'side': side,
                                            'type': 'LIMIT',
                                            'price': round(price, self.prise_precision),
                                            'quantity': quantity})
                self.id_buy_positions[index] = order["orderId"]
            elif side == "SELL":
                order = cp.create_position({'symbol': self.coin_pair,
                                            'side': side,
                                            'type': 'LIMIT',
                                            'price': round(price, self.prise_precision),
                                            'quantity': quantity})

                self.id_sell_positions[index] = order["orderId"]
        except Exception as e:
            print("ставка не сработала", e)
            time.sleep(10)
            self.create_position(price, side, index)

    def order_buy_positions(self):
        deep_buys = DEEP_ORDERS
        for i in range(len(self.balancer)):
            if self.balancer[i] >= 0:
                if self.id_buy_positions[i] is not None:
                    close_order_with_id(self.coin_pair, self.id_buy_positions[i])
                if deep_buys:
                    deep_buys -= 1
                else:
                    break
                self.create_position(self.buy_prices[i], "BUY", i)

    def order_sell_positions(self):
        deep_sell = DEEP_ORDERS
        for i in range(len(self.balancer)):
            if self.balancer[i] <= 0:
                if self.id_sell_positions[i] is not None:
                    close_order_with_id(self.coin_pair, self.id_sell_positions[i])
                if deep_sell:
                    deep_sell -= 1
                else:
                    break
                self.create_position(self.sell_prices[i], "SELL", i)

    def create_all_positions(self, kline):  # [время открытия, открытие, максимум свечи, минимум свечи, закрытие, объем]
        top_price = float(kline[2])
        bottom_price = float(kline[3])
        buy_price = round(top_price * ((100 - self.band_size[0]) / 100), self.prise_precision)
        sell_price = round(bottom_price * ((100 + self.band_size[0]) / 100), self.prise_precision)

        if buy_price > self.buy_prices[0] or self.rebalanser == 1:
            self.rebalanser = 0
            for i in range(len(self.balancer)):
                if self.balancer[i] >= 0:
                    buy_price = round(top_price * ((100 - self.band_size[i]) / 100), self.prise_precision)

                    self.buy_prices[i] = buy_price
                    top_price = buy_price
            self.order_buy_positions()
            print("BUY", self.buy_prices)

        if sell_price < self.sell_prices[0] or self.rebalanser == -1:
            self.rebalanser = 0
            for i in range(len(self.balancer)):
                if self.balancer[i] <= 0:
                    sell_price = round(bottom_price * ((100 + self.band_size[i]) / 100), self.prise_precision)

                    self.sell_prices[i] = sell_price
                    bottom_price = sell_price
            self.order_sell_positions()
            print("SELL", self.sell_prices)

    def change_balanser(self, orderid, side):
        if side == 'BUY':
            order_index = self.id_buy_positions.index(orderid)
            self.rebalanser = -1 if order_index == 0 else 0
            self.balancer[order_index] = -1
            self.id_buy_positions[order_index] = None
        else:
            order_index = self.id_sell_positions.index(orderid)
            self.rebalanser = 1 if order_index == 0 else 0
            self.balancer[order_index] = 1
            self.id_sell_positions[order_index] = None
        print('Изменяем баланс', self.coin_pair, self.balancer)


all_vars = []

for i in COIN_PAIRS:
    i = Variant(i, PRICE_PRECISION[i], LOT_SIZE[i])
    all_vars.append(i)


def options_for_functions(foo, sec, args, after=True):
    while True:
        if after:
            foo(*args)
            time.sleep(sec)
        else:
            time.sleep(sec)
            foo(*args)


def kline_try(coin):
    try:
        return ma.get_klines(coin)[-1]
    except Exception as e:
        print(e)
        time.sleep(10)
        kline_try(coin)


def get_acc_balace():
    global BALANCE
    try:
        BALANCE = float(cp.get_acc_balace())
    except Exception as e:
        print(e)
        time.sleep(10)
        get_acc_balace()


def begin_all_vars():
    get_acc_balace()
    print(BALANCE)
    prices = {}
    for coin in COIN_PAIRS:
        prices[coin] = kline_try(coin)
        if prices[coin] is None:
            prices[coin] = kline_try(coin)
    for i in all_vars:
        i.create_all_positions(prices[i.coin_pair])


def message_handler(_, message):
    data_2 = json.JSONDecoder().decode(message)
    if data_2['e'] and data_2['e'] == 'ORDER_TRADE_UPDATE':
        side = data_2['o']['S']
        order_id = data_2['o']['i']
        if data_2['o']['x'] == 'TRADE':
            for i in all_vars:
                if order_id in i.id_buy_positions or order_id in i.id_sell_positions:
                    i.change_balanser(order_id, side)


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
