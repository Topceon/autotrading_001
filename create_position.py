import requests

import marker_actions as ma


def create_position(order):
    if order["type"] == "LIMIT":
        ma.limit_pos(order)

    if order['type'] == 'MARKET':
        ma.market_pos(order)

    if order['type'] == 'STOP_MARKET':
        ma.stop_market(order)

    if order['type'] == 'CancelOrder':
        ma.cancel_order(order)

        url_order = "/fapi/v1/allOpenOrders"


if __name__ == '__main__':
    # отложенная заявка срабатывает сразу если цена лучше чем в заявке
    create_position({'symbol': 'GMTUSDT', 'side': 'BUY', 'type': 'LIMIT', 'price': 0.301, 'quantity': 35})
    # покупка по маркету
    # create_position({'symbol': 'BLZUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 35})
    # снимает все отложенные заявки для этой пары
    # create_position({'symbol':'BLZUSDT', 'type': 'CancelOrder'})
    # закрывает ордер по указанной цене, если позиция SELL то и STOP_MARKET в плюс SELL а в минус BUY
    # закрывает ордер по указанной цене, если позиция BUY то и STOP_MARKET в плюс BUY а в минус SELL
    # create_position({'symbol':'BLZUSDT', 'type': 'STOP_MARKET', 'stopprice': 0.357, 'side': 'BUY', 'closePosition': 'true', 'quantity': 'Close-All'})
    # увеличивает позицию отложкой по целевой цене если дано quantity, closePosition не равно true
    # create_position({'symbol': 'ARBUSDT', 'type': 'STOP_MARKET', 'side': 'SELL', 'stopprice': 1.7018, 'quantity': 8})
    # проверка аккаунта
    # create_position({'acc': 'acc'})
    # print(query_new_prices())
