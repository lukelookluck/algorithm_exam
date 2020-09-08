import sys
sys.stdin = open('미로.txt')

def my_func(start_x, start_y):
    global N, result
    arr[start_x][start_y] = 1

    for i in range(4):
        if (0 <= start_x + dx[i] < N and 0 <= start_y + dy[i] < N):
            if arr[start_x + dx[i]][start_y + dy[i]] == 3:
                result = 1
                return

            if arr[start_x + dx[i]][start_y + dy[i]] == 0:
                my_func(start_x + dx[i], start_y + dy[i])

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                my_func(i, j)

    print("#{} {}".format(tc + 1, result))