import sys
from collections import deque


def solution(x, y):
    for d in range(4):
        new_x, new_y = x + dx[d], y + dy[d]
        if 0 <= new_x < N and 0 <= new_y < M and my_arr[new_x][new_y] and check[new_x][new_y] == 0:
            to_go.append((new_x, new_y))
            check[new_x][new_y] = check[x][y] + 1




N, M = map(int, sys.stdin.readline().split())
my_arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
to_go = deque()
to_go.append((0, 0))
check[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while to_go:
    x, y = map(int, to_go.popleft())
    solution(x, y)

print(check[N-1][M-1])

