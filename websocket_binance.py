import threading
import time
import logging
from binance.lib.utils import config_logging
from binance.um_futures import UMFutures
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
import keys
import json

import main_app

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
BALANCER = {COIN: 0 for COIN in COIN_PAIR}


# config_logging(logging, logging.DEBUG)

def foo():
    global BALANCER
    main_app.run_main_app(COIN_PAIR, BALANCER)


def message_handler(_, message):
    global BALANCER
    # main_app.run_main_app(COIN_PAIR)
    # time.sleep(30)
    data_2 = json.JSONDecoder().decode(message)
    print(data_2)
    if data_2['e'] and data_2['e'] == 'ORDER_TRADE_UPDATE':
        print(data_2['o']['x'])
        if data_2['o']['x'] == 'TRADE':
            if data_2['o']['S'] == 'BUY':
                BALANCER[data_2['o']['s']] = -1
            else:
                BALANCER[data_2['o']['s']] = 1
        # main_app.run_main_app(COIN_PAIR, BALANCE)
    print(BALANCER)


api_key = keys.API_key
client = UMFutures(api_key)
response = client.new_listen_key()
print(response)


def new_listen_key():
    global response
    api_key = keys.API_key
    client = UMFutures(api_key)
    response = client.new_listen_key()


# logging.info("Listen key : {}".format(response["listenKey"]))
def activity():
    ws_client = UMFuturesWebsocketClient(on_message=message_handler)

    ws_client.user_data(
        listen_key=response["listenKey"],
        id=1
    )


def activity1():
    time.sleep(3500)
    new_listen_key()


def activity2():
    foo()
    time.sleep(300)


if __name__ == '__main__':
    list1 = [activity, activity1, activity2]

    threads = [threading.Thread(target=i, daemon=True) for i in list1]
    for e in threads:
        e.start()
    for e in threads:
        e.join()
    # logging.debug("closing ws connection")
    # ws_client.stop()
