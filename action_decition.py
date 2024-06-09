def lot_size_precision(a):
    precision = 0
    for i in str(a):
        if i == '1':
            return precision
        elif i == '.':
            pass
        else:
            precision += 1


if __name__ == '__main__':
    print(lot_size_precision('0.0000000001'))
