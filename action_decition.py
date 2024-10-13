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
    with open("config.txt", "r") as file:
        balansers = json.load(file)
    return balansers

def get_balanser_for_file(balansers):
    with open("config.txt", "w") as file:
        json.dump(balansers, file)


if __name__ == '__main__':
    print(len(get_balanser_from_file()["XRPUSDT"]))
    # print(lot_size_precision('0.0000000001'))
