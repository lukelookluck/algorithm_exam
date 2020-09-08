import sys
sys.stdin = open('정사각형 방.txt')

import sys
sys.setrecursionlimit(2600)

def my_func(i, j, count, result):
    global my_result, my_max, p

    # if count < my_max:
    #     return
    for k in range(4):
        if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N and arr[i + dx[k]][j + dy[k]] == arr[i][j] + 1:
            used[i+dx[k]][j+dy[k]] = 1
            my_func(i + dx[k], j + dy[k], count + 1, result)
    if my_max < count:
        my_max = count
        my_result = []
        my_result += [result]
    if my_max == count:
        my_result += [result]
    # for k in range(4):
    #     if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
    #         if arr[i+dx[k]][j+dy[k]] == arr[i][j] +1:
    #             my_func(i+dx[k], j+dy[k], count+1, result)
    # print(my_max)
    # print(my_result)

    # if my_result >= result and my_max == result:


    # print(result, count)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    my_max = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    my_result = []
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if used[i][j] != 1:

                my_func(i, j, 1, arr[i][j])
    # print(my_result)
    print("#{} {} {}".format(tc+1, min(my_result), my_max))
    # print("재귀횟수 {} 번".format(p))