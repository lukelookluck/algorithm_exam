def itoa(x):
    str = list()
    y = 0, 0
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10

    str.reversed''

