import sys


def find(i, j):
    if not check2[i][j]:
        return []

    return find(i, check2[i][j]) + [check2[i][j]] + find(check2[i][j], j)


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
check = [[float('inf')] * (n+1) for _ in range(n+1)]
check2 = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    check[a][b] = min(c, check[a][b])

for x in range(1, n+1):
    check[x][x] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if check[i][j] > check[x][j] + check[i][x]:
                check[i][j] = check[x][j] + check[i][x]
                check2[i][j] = x

for i in range(1, n+1):
    for j in range(1, n+1):
        if check[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(check[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if check[i][j] == float('inf') or check[i][j] == 0:
            print(0)
        else:
            answer = [i] + find(i, j) + [j]
            print(len(answer), *answer)