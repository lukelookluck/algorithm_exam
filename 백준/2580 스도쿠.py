import sys


def solution(cnt):
    if cnt == len(zero_list):
        for dt in data:
            print(*dt)
        sys.exit(0)

    check = [0] * 10
    x, y = zero_list[cnt][0], zero_list[cnt][1]

    for a in range(9):
        if data[x][a]:
            check[data[x][a]] = 1
        if data[a][y]:
            check[data[a][y]] = 1

    for a in range(3):
        for b in range(3):
            if data[x//3*3 + a][y//3*3 + b]:
                check[data[x//3*3 + a][y//3*3 + b]] = 1

    result = []
    for i in range(1, 10):
        if check[i] == 0:
            result.append(i)
    for rs in result:
        data[x][y] = rs
        solution(cnt + 1)
        data[x][y] = 0


data = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero_list = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            zero_list.append((i, j))

solution(0)