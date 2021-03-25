import sys


V, E = map(int, sys.stdin.readline().split())
inf = float('inf')
arr = [[inf] * (V+1) for _ in range(V+1)]
answer = inf

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a][b] = c

for x in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min((arr[i][j], arr[i][x] + arr[x][j]))

    answer = min(answer, arr[x][x])

print(answer if answer != inf else -1)