import json


def lot_size_precision(a):
    precision = 0
    for i in str(a):
        if i == '1':
            return precision
        elif i == '.':
            pass
        else:
            precision += 1


def get_balanser_from_file():
    with open("vol/config.txt", "r") as file:
        balansers = json.load(file)
    return balansers

def get_balanser_for_file(balansers):
    with open("vol/config.txt", "w") as file:
        json.dump(balansers, file)

def get_coins_from_file():
    with open("vol/coins.txt", "r") as file:
        coins = json.loads(file.readline())
    return coins

if __name__ == '__main__':
    a = get_coins_from_file()
    print(a)
    print(type(a))
    # print(lot_size_precision('0.0000000001'))
