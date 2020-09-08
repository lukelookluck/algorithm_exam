import sys
sys.stdin = open('피자 굽기.txt')

def my_func(n, d, q):
    global result
    if d == [0]*N:
        return
    if arr:
        if not my_q[n%N]:
            my_q[n%N] = arr.pop(0)
            my_q2[n%N] = q
            my_func(n+1, my_q, q+1)
        else:
            my_q[n%N] //= 2
            if my_q[n%N]:
                my_func(n+1, my_q, q)
            else:
                my_func(n, my_q, q)
    else:
        my_q[n%N] //= 2
        result = my_q2[n%N]
        my_func(n+1, my_q, q)

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    my_q = [0] * N
    my_q2 = [0] * N
    my_q[0] = arr.pop(0)
    my_q2[0] = 0
    result = 0
    my_func(1, 0, 1)
    print("#{} {}".format(tc+1, result+1))