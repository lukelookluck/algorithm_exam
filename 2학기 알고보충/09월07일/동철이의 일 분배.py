import sys
sys.stdin = open('동철이의 일 분배.txt')


def my_func(n, my_sum):
    global answer

    if my_sum <= answer:
        return

    if n == N:
        answer = my_sum
        return

    else:
        for i in range(N):
            if used[i] != 1:
                used[i] = 1
                my_func(n+1, my_sum*arr[n][i]*0.01)
                used[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = float('-inf')
    used = [0]*N
    my_func(0, 1)
    print("#{} {:.6f}".format(tc+1, answer*100))