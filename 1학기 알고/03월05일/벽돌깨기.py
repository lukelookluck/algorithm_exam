import sys
sys.stdin = open('벽돌깨기.txt')


def combinations(data, r):
    for i in range(len(data)):
        if r == 1:
            yield [data[i]]
        else:
            for c in combinations(data, r - 1):
                yield [data[i]] + c


def break_wall(column):
    for i in range(H):
        if arr[i][column] != 0:
            my_scale = arr[i][column]
            aftershock(i, column, my_scale)
            break

    for j in range(W):
        for i in range(H - 1, -1, -1):
            q = i
            while q > 0 and arr[q][j] == 0:
                q -= 1
            if q != i:
                arr[i][j] = arr[q][j]
                arr[q][j] = 0


def aftershock(i, column, my_scale):
    arr[i][column] = 0
    for m in range(0, my_scale):
        for k in range(4):
            if 0 <= i + dx[k] * m < H and 0 <= column + dy[k] * m < W:
                if arr[i + dx[k] * m][column + dy[k] * m] > 1:
                    aftershock(i + dx[k] * m, column + dy[k] * m, arr[i + dx[k] * m][column + dy[k] * m])
                else:
                    arr[i + dx[k] * m][column + dy[k] * m] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    arr_clone = [list(map(int, input().split())) for _ in range(H)]
    arr = [[0] * W for _ in range(H)]
    my_min = float('inf')
    for combi in combinations(list(range(W)), N):
        for k in range(H):
            for m in range(W):
                arr[k][m] = arr_clone[k][m]
        for z in combi:
            break_wall(z)
            cnt = 0
            for k in range(H):
                for m in range(W):
                    if arr[k][m] != 0:
                        cnt += 1
            if my_min > cnt:
                my_min = cnt
    print("#{} {}".format(tc + 1, my_min))
