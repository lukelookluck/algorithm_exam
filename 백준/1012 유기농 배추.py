from collections import deque
import sys


T = int(sys.stdin.readline().strip())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    to_go = []

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1
        to_go.append((a, b))

    answer = 0

    for to in to_go:
        j, i = to
        if check[i][j] == 0:
            my_deq = deque([(i, j)])
            check[i][j] = 1

            while my_deq:
                x, y = my_deq.popleft()
                for i in range(4):
                    new_x, new_y = x + dx[i], y + dy[i]
                    if 0 <= new_x < N and 0 <= new_y < M:
                        if arr[new_x][new_y] == 1 and check[new_x][new_y] == 0:
                            check[new_x][new_y] = 1
                            my_deq.append((new_x, new_y))
            answer += 1

    print(answer)