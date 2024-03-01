import requests


def query_new_prices() -> dict:
    resp = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    a = resp.json()
    d = {i['symbol']: float(i['price']) for i in a if i['symbol'][-4:] != 'BUSD'}
    return d




if __name__ == '__main__':
    pass