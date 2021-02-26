import sys

N, M = map(int, sys.stdin.readline().split())
arr1, arr2 = [], []

for _ in range(N):
    arr1.append(list(map(int, sys.stdin.readline().split())))

A, B = map(int, sys.stdin.readline().split())

for _ in range(A):
    arr2.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * B for _ in range(N)]

for n in range(N): # 0 1 2
    for m in range(B): # 0 1 2
        for a in range(A): # 0 1
            result[n][m] += arr1[n][a] * arr2[a][m]

for rs in result:
    print(*rs)