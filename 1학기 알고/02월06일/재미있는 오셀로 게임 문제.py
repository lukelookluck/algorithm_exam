import sys
sys.stdin = open('재미있는 오셀로 게임.txt')

def my_func(x, y, color, i):
    if not (0 <= x < N and 0 <= y < N) or arr[y][x] == 0:
        return False
    elif arr[y][x] == color:
        return True
    else:
        if my_func(x + dx[i], y + dy[i], color, i) == True:
            arr[y][x] = color
            return True

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]



    for m in range(M):
        y, x, color = map(int, input().split())
        x -= 1
        y -= 1
        arr[y][x] = color
        for i in range(8):
            my_func(x + dx[i], y + dy[i], color, i)

    black = white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1

            elif arr[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc+1, black, white))