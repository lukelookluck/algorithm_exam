def solution(prices):
    answer = []

    n = 0
    while n < len(prices):
        x = prices[n]
        cnt = 0

        for i in range(n+1, len(prices)):
            cnt += 1
            if x > prices[i]:
                break

        answer.append(cnt)
        n += 1

    return answer


p = [1, 2, 3, 2, 2, 3]
print(solution(p))