def f(n,a,b):
    if n == N:
        for i in range(N):
            print(A,B)
            return

    else:
        for i in range(N):
            if not u[i] :
                u[i] = 1
                A[n] = i
                f(n+1,a+1,b)
                A[n] = 0
                u[i] = 0
            if not u[i]:
                u[i] = 1
                B[n] = i
                f(n+1,a,b + 1)
                B[n] = 0
                u[i] = 0


T = 1
for tc in range(1,T+1):
    N = 4
    A = [0] * 4
    B = [0] * 4
    u = [0]*N
    # ing = [list(map(int,input().split())) for _ in range(N)]

    f(0,0,0)