import websocket
import requests
import threading
import time
import json

import keys
import main_app as rv

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
BALANCER = {COIN: 0 for COIN in COIN_PAIR}


def options_for_functions(foo, sec, args, after=True):
    while True:
        if after:
            foo(*args)
            time.sleep(sec)
        else:
            time.sleep(sec)
            foo(*args)


def message_handler(_, message):
    global BALANCER
    data_2 = json.JSONDecoder().decode(message)
    print(data_2)
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

list_of_function = []


def start_ws():
    while True:
        try:
            ws = websocket.WebSocketApp('wss://fstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice',
                                        on_message=message_handler)
            ws.run_forever()
            print('Test')
            time.sleep(5)
        except Exception as e:
            print('Проблема сокета', e)
            time.sleep(5)


def renew_listen_key():
    options_for_functions(new_listen_key, 3500, [], after=False)


def start_strategy_2():
    options_for_functions(rv.run_main_app, 300, [COIN_PAIR, BALANCER])


def start_strategy_3():
    options_for_functions(rv.run_variation, 30, ['test', 23])


functions_for_start = [start_ws,
                       renew_listen_key
                       ]

threads = [threading.Thread(target=i, daemon=True) for i in functions_for_start]
for e in threads:
    e.start()
for e in threads:
    e.join()

if __name__ == '__main__':
    pass
