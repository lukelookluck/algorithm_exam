from collections import deque
import sys



N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
check = [[[-1]*2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


my_d = deque()
my_d.append((0, 0, 1))
check[0][0][1] = 1

while my_d:
    # print(my_d)
    # print(*check, sep='\n')

    x, y, crush = my_d.popleft()

    if x == N-1 and y == M-1:
        break
    # print('현재', x, y)

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M:
            if arr[new_x][new_y] == 1 and crush == 1:
                check[new_x][new_y][0] = check[x][y][1] + 1
                my_d.append((new_x, new_y, 0))
            elif arr[new_x][new_y] == 0 and check[new_x][new_y][crush] == -1:
                check[new_x][new_y][crush] = check[x][y][crush] + 1
                my_d.append((new_x, new_y, crush))


print(max(check[N-1][M-1]))