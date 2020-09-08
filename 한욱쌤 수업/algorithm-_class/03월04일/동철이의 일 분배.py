import sys
sys.stdin = open('동철이의 일 분배.txt')

def my_func(y):
    global my_sum, no_dab
    print(no_dab, my_sum)
    if no_dab <= my_sum:
        return

    if y == N:
        my_sum = no_dab
        return
    else:
        for i in range(N):
            if used[i] != 1:
                if arr[y][i] == 0:
                    continue
                no_dab *= arr[y][i]/100
                used[i] = 1
                my_func(y+1)
                used[i] = 0
                no_dab /= arr[y][i]/100


T = int(input())
for tc in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    no_dab, my_sum = 1, float('-inf')
    my_func(0)
    print("#{} {:.6f}".format(tc + 1, my_sum * 100))