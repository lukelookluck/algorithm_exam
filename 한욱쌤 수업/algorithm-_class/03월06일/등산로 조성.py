import sys
sys.stdin = open('등산로 조성.txt')

def my_func(i, j, count, cut, q):
    global my_count
    for k in range(4):
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
            if arr[i][j] > arr[i+dx[k]][j+dy[k]] and used[i+dx[k]][j+dy[k]] == 0:
                used[i+dx[k]][j+dy[k]] = 1
                my_func(i+dx[k], j+dy[k], count+1, cut, q)
                used[i + dx[k]][j + dy[k]] = 0

            elif arr[i][j] > arr[i+dx[k]][j+dy[k]] - q and cut > 0 and used[i+dx[k]][j+dy[k]] == 0:
                arr[i + dx[k]][j + dy[k]] = arr[i+dx[k]][j+dy[k]] - q
                used[i+dx[k]][j+dy[k]] = 1
                my_func(i+dx[k], j+dy[k], count+1, cut-1, q)
                used[i + dx[k]][j + dy[k]] = 0
                arr[i + dx[k]][j + dy[k]] = arr[i + dx[k]][j + dy[k]] + q
    if my_count < count:
        my_count = count





dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr = [[0] * N for _ in range(N)]
    used = [[0] * N for _ in range(N)]
    my_max = float('-inf')
    my_count = float('-inf')

    for i in range(N):
        for j in range(N):
            if my_max < arr[i][j]:
                my_max = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == my_max:
                # for k in range(N):
                #     for m in range(N):
                #         arr[k][m] = arr_ori[k][m]
                # print(arr)
                for q in range(1, K+1):
                    used[i][j] = 1
                    my_func(i, j, 1, 1, q)
                    used[i][j] = 0
    # print(count)
    print("#{} {}".format(tc+1, my_count))


