import get_data_from_market as dm
import strategy_2 as sg
import create_position as cp

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
POSITION_SIZE = 10  # размер позиции в процентах от депозита


def get_data_from_market(coin_pair):
    data = dm.get_data(coin_pair)
    return data


def strategy(data, balancer):
    data = sg.strategy(data, balancer)
    return data


def create_positions(list_data):
    for data in list_data:
        cp.create_position(data)


def run_main_app(coin_pair, balancer={}):
    data = get_data_from_market(coin_pair)
    list_data = strategy(data, balancer)
    create_positions(list_data)


if __name__ == '__main__':
    run_main_app(COIN_PAIR)
