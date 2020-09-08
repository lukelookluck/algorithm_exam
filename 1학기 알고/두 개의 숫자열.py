import sys
sys.stdin = open('두 개의 숫자열.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    dataA = list(map(int, input().split()))
    dataB = list(map(int, input().split()))


    if N > M:
        result = -112635411263511233112353115131213162531
        for i in range(N - M + 1):
            result2 = 0
            for j in range(M):
                result2 += dataA[i+j] * dataB[j]
            if result2 > result:
                result = result2
    else:
        result = -112635411263511233112353115131213162531
        for i in range(M - N + 1):
            result2 = 0
            for j in range(N):
                result2 += dataB[i + j] * dataA[j]
            if result2 > result:
                result = result2

    print(result)