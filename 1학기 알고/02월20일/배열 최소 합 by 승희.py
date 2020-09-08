import sys
sys.stdin = open('../../기술/임시/순열.txt')


def permutation(k, N, my_sum):
    global my_min

    if my_sum >= my_min:
        return

    if k == N:
        if my_sum < my_min:
            my_min = my_sum
            return

    else:
        for i in range(k, N):
            arr[i], arr[k] = arr[k], arr[i]
            permutation(k+1, N, my_sum+data[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(range(N))
    data = [list(map(int, input().split())) for _ in range(N)]
    my_min = float('inf')

    permutation(0, N, 0)
    print("#{} {}".format(tc+1, my_min))