import sys

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort()
check = [1] * N

for i in range(N-1, -1, -1):
    mymax = 0
    for j in range(i, N):
        if arr[j][1] > arr[i][1] and check[j] > mymax:
            mymax = check[j]
    check[i] += mymax

print(N - max(check))