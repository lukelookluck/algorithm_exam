import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # print(arr)
    for i in range(N):
        before_rc = 0
        for j in range(N):
            if arr[i][j] == 0:
                before_rc = 0
                continue
            if before_rc == 1:
                continue
            else:
                count = 0
                k = j
                while k < N and arr[i][k] == 1:
                    before_rc = 1
                    count += 1
                    k += 1
                if count == K:
                    result += 1

    for i in range(N):
        before_rc = 0
        for j in range(N):
            if arr[j][i] == 0:
                before_rc = 0
                continue
            if before_rc == 1:
                continue
            else:
                count = 0
                k = j
                while k < N and arr[k][i] == 1:
                    before_rc = 1
                    count += 1
                    k += 1
                if count == K:
                    result += 1


    print("#{} {}".format(tc+1, result))