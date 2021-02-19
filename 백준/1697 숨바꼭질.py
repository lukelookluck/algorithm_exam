import sys


def solution(N, K):
    result = [N]
    check[N] = 1
    ans = 0

    while result:
        temp = []
        for re in result:
            if 0 <= re-1 <= 100000:
                if check[re-1] == 0:
                    check[re-1] = 1
                    temp.append(re-1)
            if 0 <= re+1 <= 100000:
                if check[re+1] == 0:
                    check[re+1] = 1
                    temp.append(re+1)
            if 0 <= re*2 <= 100000:
                if check[re*2] == 0:
                    check[re*2] = 1
                    temp.append(re*2)
            if re == K:
                return ans

        # print(temp)
        result = temp
        ans += 1


N, K = map(int, sys.stdin.readline().split())
check = [0] * 100001
print(solution(N, K))
