import sys
sys.stdin = open('숫자 배열 회전.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result_arr = [[0 for _ in range(N)] for _ in range(N)]
    result_arr2 = [[0 for _ in range(N)] for _ in range(N)]
    result_arr3 = [[0 for _ in range(N)] for _ in range(N)]


    # 90도
    for i in range(N):
        for j in range(N):
            result_arr[j][(N-1)-i] = arr[i][j]

    # 벤: 180도
    for i in range(N):
        for j in range(N):
            result_arr2[(N-1)-i][(N-1)-j] = arr[i][j]

    # 270도
    for i in range(N):
        for j in range(N):
            result_arr3[(N-1)-j][i] = arr[i][j]

    print("#{}".format(tc+1))
    for i in range(N):
        print(*result_arr[i], sep='', end=' ')
        print(*result_arr2[i], sep='', end=' ')
        print(*result_arr3[i], sep='')
