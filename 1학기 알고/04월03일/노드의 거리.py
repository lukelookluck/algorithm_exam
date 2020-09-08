import sys
sys.stdin = open('노드의 거리.txt')

def my_func(x, cnt):
    global result, my_bool

    for i in range(V):
        if cnt > result:
            return
        if arr[x][i] == 1 and i == f_c-1:
            my_bool = True
            if result > cnt:
                result = cnt
            return
        if arr[x][i] == 1:
            arr[x][i] = 0
            arr[i][x] = 0
            my_func(i, cnt+1)
            arr[x][i] = 1
            arr[i][x] = 1

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0]*V for _ in range(V)]
    my_bool = False
    result = float('inf')

    for e in range(E):
        t_r, t_c = map(int, input().split())
        arr[t_r -1][t_c -1] = 1
        arr[t_c -1][t_r -1] = 1
    f_r, f_c = map(int, input().split())

    my_func(f_r-1, 0)

    if my_bool == True:
        print("#{} {}".format(tc+1, result+1))
    else:
        print("#{} {}".format(tc + 1, 0))
