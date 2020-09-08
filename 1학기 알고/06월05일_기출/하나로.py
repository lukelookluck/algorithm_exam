import sys, time
sys.stdin = open('하나로.txt')


def my_func(x):
    my_min = float('inf')
    for i in range(N):
        if my_min > arr[x][i] != 0 and check_list[i] != 1:
            my_min = arr[x][i]
    result.append(my_min)
    print(result)
    my_func(x+1)



T = int(input())
for tc in range(T):
    N = int(input())
    dx = [*map(int, input().split())]
    dy = [*map(int, input().split())]
    E = float(input())
    check_list = [0]*N
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[j][i] = (dx[i] - dx[j]) ** 2 + (dy[i] - dy[j]) ** 2
    for i in arr:
        print(i)
    result = []
    check_list[0] = 1

    my_func(1)
    print("#{} {}".format(tc+1, round(result)))