import sys
sys.stdin = open('회문.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    my_str = []
    # 가로 탐색
    for i in range(N):
        for j in range(0, N - (M - 1)):
        # if M % 2 == 0:
            for k in range(0, M // 2):
                if arr[i][j + k] == arr[i][j + (M - 1) - k]:
                    result = 1
                else:
                    result = 0
                    break
        if result == 1:
            for m in range(M):
                my_str.append(arr[i][j+m])

    # 세로 탐색
    for i in range(N):
        for j in range(0, N - (M - 1)):
        # if M % 2 == 0:
            for k in range(0, M // 2):
                if arr[j + k][i] == arr[j + (M - 1) - k][i]:
                    result = 1
                else:
                    result = 0
                    break
        if result == 1:
            for m in range(M):
                my_str.append(arr[j+m][i])



    print("#{}".format(tc+1), end=' ')

    for i in my_str:
        print(i, end='')
    print()
