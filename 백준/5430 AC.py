import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    my_f = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    data = sys.stdin.readline().strip()[1:-1].split(',')

    rev = False
    f, b = 0, 0

    for ff in my_f:
        if ff == 'R':
            rev = True if not rev else False

        else:
            if rev:
                b += 1
            else:
                f += 1

    if f + b > n:
        print('error')
    else:
        data = data[f:n - b]
        if rev:
            print('[' + ','.join(data[::-1]) + ']')
        else:
            print('[' + ','.join(data) + ']')