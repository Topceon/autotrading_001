import websocket
import requests
import threading
import time
import json

import keys
import main_app

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
BALANCER = {COIN: 0 for COIN in COIN_PAIR}


def foo():
    global BALANCER
    main_app.run_main_app(COIN_PAIR, BALANCER)


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


def activity():
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


def activity1():
    while True:
        time.sleep(3500)
        new_listen_key()


def activity2():
    while True:
        foo()
        time.sleep(300)


if __name__ == '__main__':
    list1 = [activity,
             activity1,
             activity2
             ]

    threads = [threading.Thread(target=i, daemon=True) for i in list1]
    for e in threads:
        e.start()
    for e in threads:
        e.join()
