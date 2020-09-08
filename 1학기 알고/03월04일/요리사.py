import sys
sys.stdin = open('요리사.txt')

def combination(n, k, a, b):
    global no_dab_A, no_dab_B, my_min
    if n == k:
        for i in A:
            for j in A:
                no_dab_A += arr[i][j]
        for i in B:
            for j in B:
                no_dab_B += arr[i][j]
        if my_min > abs(no_dab_A - no_dab_B):
            my_min = abs(no_dab_A - no_dab_B)
        no_dab_A, no_dab_B = 0, 0
        return
    else:
        if a < k // 2:
            A.append(n)
            # no_dab_A += arr[n][n]
            combination(n+1, k, a+1, b)
            A.pop()
        if b < k // 2:
            B.append(n)
            # no_dab_B += arr[n][n]
            combination(n+1, k, a, b+1)
            B.pop()



T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = [0]
    B = []
    no_dab_A, no_dab_B, my_min = 0, 0, float('inf')

    combination(1, N, 1, 0)
    print("#{} {}".format(tc+1, my_min))