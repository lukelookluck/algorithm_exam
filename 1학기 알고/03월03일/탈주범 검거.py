import sys
sys.stdin = open('탈주범 검거.txt')

def my_func(i, j, count, a):
    global cnt

    if a == L:
        return

    if used[i][j] == 0:
        used[i][j] = 1

        if used2[i][j] == 0:
            used2[i][j] = 1
            cnt += 1

        if arr[i][j] == 1:
            if 0 <= i+dx_1[0] < N and 0 <= j+dy_1[0] < M and arr[i+dx_1[0]][j+dy_1[0]] in [1, 2, 5, 6]:
                my_func(i+dx_1[0], j+dy_1[0], count+1, a+1)
            if 0 <= i+dx_1[1] < N and 0 <= j+dy_1[1] < M and arr[i+dx_1[1]][j+dy_1[1]] in [1, 2, 4, 7]:
                my_func(i+dx_1[1], j+dy_1[1], count+1, a+1)
            if 0 <= i+dx_1[2] < N and 0 <= j+dy_1[2] < M and arr[i+dx_1[2]][j+dy_1[2]] in [1, 3, 4, 5]:
                my_func(i+dx_1[2], j+dy_1[2], count+1, a+1)
            if 0 <= i+dx_1[3] < N and 0 <= j+dy_1[3] < M and arr[i+dx_1[3]][j+dy_1[3]] in [1, 3, 6, 7]:
                my_func(i+dx_1[3], j+dy_1[3], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 2:
            if 0 <= i+dx_2[0] < N and 0 <= j+dy_2[0] < M and arr[i+dx_2[0]][j+dy_2[0]] in [1, 2, 5, 6]:
                my_func(i+dx_2[0], j+dy_2[0], count+1, a+1)
            if 0 <= i+dx_2[1] < N and 0 <= j+dy_2[1] < M and arr[i+dx_2[1]][j+dy_2[1]] in [1, 2, 4, 7]:
                my_func(i+dx_2[1], j+dy_2[1], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 3:
            if 0 <= i+dx_3[0] < N and 0 <= j+dy_3[0] < M and arr[i+dx_3[0]][j+dy_3[0]] in [1, 3, 4, 5]:
                my_func(i+dx_3[0], j+dy_3[0], count+1, a+1)
            if 0 <= i+dx_3[1] < N and 0 <= j+dy_3[1] < M and arr[i+dx_3[1]][j+dy_3[1]] in [1, 3, 6, 7]:
                my_func(i+dx_3[1], j+dy_3[1], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 4:
            if 0 <= i+dx_4[0] < N and 0 <= j+dy_4[0] < M and arr[i+dx_4[0]][j+dy_4[0]] in [1, 2, 5, 6]:
                my_func(i+dx_4[0], j+dy_4[0], count+1, a+1)
            if 0 <= i+dx_4[1] < N and 0 <= j+dy_4[1] < M and arr[i+dx_4[1]][j+dy_4[1]] in [1, 3, 6, 7]:
                my_func(i+dx_4[1], j+dy_4[1], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 5:
            if 0 <= i+dx_5[0] < N and 0 <= j+dy_5[0] < M and arr[i+dx_5[0]][j+dy_5[0]] in [1, 2, 4, 7]:
                my_func(i+dx_5[0], j+dy_5[0], count+1, a+1)
            if 0 <= i+dx_5[1] < N and 0 <= j+dy_5[1] < M and arr[i+dx_5[1]][j+dy_5[1]] in [1, 3, 6, 7]:
                my_func(i+dx_5[1], j+dy_5[1], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 6:
            if 0 <= i+dx_6[0] < N and 0 <= j+dy_6[0] < M and arr[i+dx_6[0]][j+dy_6[0]] in [1, 2, 4, 7]:
                my_func(i+dx_6[0], j+dy_6[0], count+1, a+1)
            if 0 <= i+dx_6[1] < N and 0 <= j+dy_6[1] < M and arr[i+dx_6[1]][j+dy_6[1]] in [1, 3, 4, 5]:
                my_func(i+dx_6[1], j+dy_6[1], count+1, a+1)
            used[i][j] = 0

        elif arr[i][j] == 7:
            if 0 <= i+dx_7[0] < N and 0 <= j+dy_7[0] < M and arr[i+dx_7[0]][j+dy_7[0]] in [1, 2, 5, 6]:
                my_func(i+dx_7[0], j+dy_7[0], count+1, a+1)
            if 0 <= i+dx_7[1] < N and 0 <= j+dy_7[1] < M and arr[i+dx_7[1]][j+dy_7[1]] in [1, 3, 4, 5]:
                my_func(i+dx_7[1], j+dy_7[1], count+1, a+1)
            used[i][j] = 0

T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(N)]
    used = [[0] * M for _ in range(N)]
    used2 = [[0] * M for _ in range(N)]

    dx_1 = [-1, 1, 0, 0]
    dy_1 = [0, 0, -1, 1]
    dx_2 = [-1, 1]
    dy_2 = [0, 0]
    dx_3 = [0, 0]
    dy_3 = [-1, 1]
    dx_4 = [-1, 0]
    dy_4 = [0, 1]
    dx_5 = [1, 0]
    dy_5 = [0, 1]
    dx_6 = [1, 0]
    dy_6 = [0, -1]
    dx_7 = [-1, 0]
    dy_7 = [0, -1]
    cnt = 0

    my_func(R, C, 0, 0)
    print("#{} {}".format(tc+1, cnt))