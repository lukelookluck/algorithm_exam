import sys
sys.stdin = open('순열.txt')


def permutation(r):
    global my_min

    if len(chosen) == r:
        my_sum = 0
        for i in range(N):
            my_sum += data[i][chosen[i]]
            if my_sum >= my_min:
                break
        if my_sum < my_min:
            my_min = my_sum
        # print(my_min)
        return

    for i in range(len(arr)):
        if used[i] != 1:
            chosen.append(arr[i])
            used[i] = 1
            permutation(r)
            used[i] = 0
            chosen.pop()


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(range(N))
    data = [list(map(int, input().split())) for _ in range(N)]
    used = [0 for _ in range(len(arr))]
    chosen = []
    my_min = float('inf')

    permutation(N)
    print("#{} {}".format(tc+1, my_min))