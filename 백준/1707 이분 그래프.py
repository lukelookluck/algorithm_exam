import sys


def solution():
    for i in range(1, V+1):
        if check[i] == 0 and len(data[i]) > 0:
            keys = [i]
            check[i] = -1
            color = 1

            while keys:
                temp = []
                for key in keys:
                    for tp in data[key]:
                        if check[tp] == 0:
                            check[tp] = color
                            temp.append(tp)

                        elif check[tp] != color:
                            return 'NO'

                color = -color
                keys = temp

    return 'YES'


K = int(sys.stdin.readline().strip())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    check = [0]*(V+1)
    data = {i: [] for i in range(1, V+1)}

    for e in range(E):
        x, y = map(int, sys.stdin.readline().split())
        data[x].append(y)
        data[y].append(x)

    print(solution())
