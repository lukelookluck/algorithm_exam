import math


def solution(progresses, speeds):
    answer = []
    left_prog = []

    for i in range(len(progresses)):
        left_prog.append(math.ceil((100 - progresses[i]) / speeds[i]))

    n = 0
    while n < len(progresses):
        x = left_prog[n]
        cnt = 1

        for i in range(n+1, len(left_prog)):
            if x >= left_prog[i]:
                cnt += 1
                n += 1
            else:
                break

        answer.append(cnt)
        n += 1

    return answer


p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p, s))