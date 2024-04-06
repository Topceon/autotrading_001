import get_data_from_market as dm
import strategy_2 as sg
import create_position as cp
import market_actions as ma

COIN_PAIR = ['1000PEPEUSDT', 'WLDUSDT']
POSITION_SIZE = 10  # размер позиции в процентах от депозита


def get_data_from_market(coin_pair):
    data = dm.get_data(coin_pair)
    return data


def strategy(data):
    data = sg.strategy(data)
    return data


def create_position(list_data):
    for data in list_data:
        cp.create_position(data)


def run_main_app(coin_pair):
    data = get_data_from_market(coin_pair)
    # while True: с задержкой
    data = strategy(data)
    create_position(data)


if __name__ == '__main__':
    run_main_app(COIN_PAIR)
