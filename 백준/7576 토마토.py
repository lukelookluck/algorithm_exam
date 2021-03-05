from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
my_deq = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
p_cnt, n_cnt = 0, 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            p_cnt += 1
            my_deq.append((i, j))
        elif arr[i][j] == -1:
            n_cnt += 1

answer = -1

while my_deq:
    temp = []
    for my in my_deq:
        x, y = my
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 0:
                p_cnt += 1
                arr[new_x][new_y] = 1
                temp.append((new_x, new_y))

    my_deq = temp
    answer += 1

if p_cnt + n_cnt == M * N:
    print(answer)
else:
    print(-1)