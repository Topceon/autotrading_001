import get_data_from_market as dm
import data_processing as dp
import action_decition as ad
import create_position as cp
import keys


COIN_PAIR = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']
POSITION_SIZE = 10  # размер позиции в процентах от депозита


def get_data_from_market(coin_pair):
    data = dm.get_data(coin_pair)
    return data


def data_processing(raw_data):
    data = dp.data_processing(raw_data)
    return data


def action_decision(list_data):
    data = ad.action_decision(list_data)
    return data


def create_position(list_data):
    data = cp.create_position(list_data)
    return data  # [{'symbol': 'BTCUSDT', 'price': 4, 'quantity': 5}]


def run_main_app(coin_pair):
    data = get_data_from_market(coin_pair)
    data = data_processing(data)
    positions = action_decision(data)
    create_position(positions)


if __name__ == '__main__':
    run_main_app(COIN_PAIR)
