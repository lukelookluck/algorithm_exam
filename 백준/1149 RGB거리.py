import sys


def solution():
    for i in range(1, N):
        data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
        data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
        data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]


N = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
solution()
print(min(data[N-1]))