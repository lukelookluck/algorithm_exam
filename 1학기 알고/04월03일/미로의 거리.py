import sys
sys.stdin = open('미로의 거리.txt.')

def my_func(i, j, cnt):
    global result
    if arr[i][j] == 3:
        print("#{} {}".format(tc+1, cnt-1))
        result = True
        return
    arr[i][j] = 1
    for k in range(4):
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N and arr[i+dx[k]][j+dy[k]] != 1:
            my_func(i+dx[k], j+dy[k], cnt+1)




T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                result = False
                my_func(i, j, 0)
    if result == False:
        print("#{} {}".format(tc+1, 0))