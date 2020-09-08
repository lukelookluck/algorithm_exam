import sys, time
sys.stdin = open('장훈이의 높은 선반.txt')

st = time.time()

def my_func(N, s, sum):
    global my_sum

    if sum >= B:
        if my_sum > sum:
            my_sum = sum
            return
        else:
            return
    if N == s:
        return
    else:
        my_func(N, s+1, sum + N_spec[s])
        my_func(N, s+1, sum)



T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    N_spec = list(map(int, input().split()))
    # check_list = [0] * N
    my_sum = float('inf')
    my_func(N, 0, 0)
    print("#{} {}".format(tc+1, my_sum - B))
print(time.time() - st)