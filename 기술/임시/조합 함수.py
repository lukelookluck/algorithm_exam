def combination(n, k, a, b):
    global no_dab_A, no_dab_B, my_min
    if n == k:
        print(A, B)
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




N = 4
A = []
B = []
no_dab_A, no_dab_B, my_min = 0, 0, float('inf')

combination(0, N, 0, 0)
    # print("#{} {}".format(tc+1, my_min))