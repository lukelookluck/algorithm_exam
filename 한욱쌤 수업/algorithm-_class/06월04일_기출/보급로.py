import sys, time

sys.stdin = open('보급로.txt')

st = time.time()

from collections import deque


def my_func():
    while my_queue:
        i, j = my_queue.popleft()
        cnt = check_arr[i][j]
        if i == N - 1 and j == N - 1:
            continue

        for d in range(4):
            temp_x = i + dx[d]
            temp_y = j + dy[d]

            if 0 <= temp_x < N and 0 <= temp_y < N and (check_arr[temp_x][temp_y] == -1 or cnt + arr[temp_x][temp_y] < check_arr[temp_x][temp_y]):
                check_arr[temp_x][temp_y] = cnt + arr[i + dx[d]][temp_y]
                my_queue.append((temp_x, temp_y))

    return check_arr[N-1][N-1]


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[*map(int, input())] for _ in range(N)]
    check_arr = [[-1] * N for _ in range(N)]
    check_arr[0][0] = arr[0][0]
    my_queue = deque()
    my_queue.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print("#{} {}".format(tc+1, my_func()))
print(time.time() - st)