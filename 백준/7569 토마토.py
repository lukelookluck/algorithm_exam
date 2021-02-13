import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
data = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
to_go = deque()
zero_cnt = 0


for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1:
                to_go.append((i, j, k, 0))
            elif data[i][j][k] == 0:
                zero_cnt += 1

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

check = 0

while to_go:
    x, y, z, days = map(int, to_go.popleft())
    for d in range(6):
        new_x, new_y, new_z = x + dx[d], y + dy[d], z + dz[d]
        if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z < M and data[new_x][new_y][new_z] == 0:
            data[new_x][new_y][new_z] = 1
            to_go.append((new_x, new_y, new_z, days + 1))
            check += 1

if check != zero_cnt:
    print(-1)
else:
    print(days)

