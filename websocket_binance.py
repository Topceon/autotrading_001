import time
import logging
from binance.lib.utils import config_logging
from binance.um_futures import UMFutures
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
import keys
import json

import main_app

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
BALANCE = {COIN: 0 for COIN in COIN_PAIR}


# config_logging(logging, logging.DEBUG)

def foo():
    global BALANCE
    main_app.run_main_app(COIN_PAIR, BALANCE)
    time.sleep(300)
    foo()


def message_handler(_, message):
    global BALANCE
    # main_app.run_main_app(COIN_PAIR)
    # time.sleep(30)
    data_2 = json.JSONDecoder().decode(message)
    print(data_2)
    if data_2['e'] and data_2['e'] == 'ORDER_TRADE_UPDATE':
        print(data_2['o']['x'])
        if data_2['o']['x'] == 'TRADE':
            if data_2['o']['S'] == 'BUY':
                BALANCE[data_2['o']['s']] = -1
            else:
                BALANCE[data_2['o']['s']] = 1
        main_app.run_main_app(COIN_PAIR, BALANCE)
    # print(BALANCE)



api_key = keys.API_key
client = UMFutures(api_key)
response = client.new_listen_key()


def new_listen_key():
    global response
    time.sleep(3500)
    api_key = keys.API_key
    client = UMFutures(api_key)
    response = client.new_listen_key()
    new_listen_key()


# logging.info("Listen key : {}".format(response["listenKey"]))


if __name__ == '__main__':
    ws_client = UMFuturesWebsocketClient(on_message=message_handler)

    ws_client.user_data(
        listen_key=response["listenKey"],
        id=1
    )
    foo()
    new_listen_key()
    # logging.debug("closing ws connection")
    # ws_client.stop()
