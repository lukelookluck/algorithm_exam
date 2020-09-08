import sys
sys.stdin = open("농작물 수확하기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    sum = []
    arr = [list(map(int, input())) for _ in range(N)]
    sum = 0
    total = 0
    for i in range(N):
        for j in range(N):
            total += arr[i][j]

    # row : 0 ~ (N // 2 -1) 까지
    k = N // 2
    for i in range(N // 2): # 0 1
        for j in range(k): # 0 1
            # for k in range(N // 2): # 2 / 123 / 01234 / 123 / 2
            sum += arr[i][j] + arr[i][(N-1) - j]
        k -= 1

    # row : (N // 2 +1) ~ N-1 까지
    k = N // 2
    for i in range(N-1, (N // 2), -1):  # 3 4
        for j in range(k):  # 0 1
            # for k in range(N // 2): # 2 / 123 / 01234 / 123 / 2
            sum += arr[i][j] + arr[i][(N - 1) - j]
        k -= 1

    # for i in sum:
    #     result += i

    print("#{} {}".format(tc+1, total - sum))