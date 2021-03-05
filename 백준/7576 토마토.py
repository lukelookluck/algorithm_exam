from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
arr = []
my_deq = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            my_deq.append((i, j))
        elif arr[i][j] == -1:
            cnt += 1

answer = -1

while my_deq:
    my_len = len(my_deq)
    for _ in range(my_len):
        x, y = my_deq.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 0:
                cnt += 1
                arr[new_x][new_y] = 1
                my_deq.append((new_x, new_y))

    answer += 1

if cnt == M * N:
    print(answer)
else:
    print(-1)