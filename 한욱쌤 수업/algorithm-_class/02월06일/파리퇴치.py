import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    arr = list(input().split() for _ in range(N))
    # print(arr)
    result2 = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for m in range(M):
                    result += (int(arr[i+k][j+m]))

            result2.append(result)





    #
    # max_result = max(result)
    print(max(result2))