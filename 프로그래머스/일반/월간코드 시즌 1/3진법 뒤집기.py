def solution(n):
    answer = 0
    base3 = ''

    while n != 0:
        base3 += str(n % 3)
        n = n // 3

    for i in range(len(base3)):
        answer += 3 ** (len(base3) - i - 1) * int(base3[i])

    return answer


n = 125
print(solution(n))