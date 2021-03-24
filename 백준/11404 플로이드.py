import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)


for k in range(n):
    arr[k][k] = 0
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for t in arr:
    for x in t:
        if x == float('inf'):
            print(0, end=' ')
        else:
            print(x, end=' ')
    print()
