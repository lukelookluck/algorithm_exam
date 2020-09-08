import sys
sys.stdin = open('회문1.txt')

T = 10
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0
    # print(arr)
    # 가로탐색
    for i in range(8):
        for j in range(0, 8-N+1):
            for k in range(N//2):
                if arr[i][j+k] == arr[i][j+N-1-k]:
                    result = 1
                else:
                    result = 0
                    break

            if result == 1:
                count += 1

    # 세로탐색
    for i in range(8):
        for j in range(0, 8 - N + 1):
            for k in range(N // 2):
                if arr[j + k][i] == arr[j+N-1-k][i]:
                    result = 1
                else:
                    result = 0
                    break

            if result == 1:
                count += 1

    print("#{} {}".format(tc+1, count))