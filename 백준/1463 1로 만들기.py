import sys


def solution(N):
    if N in answer:
        return answer[N]

    answer[N] = 1 + min(solution(N // 3) + N % 3, solution(N // 2) + N % 2)

    return answer[N]


N = int(sys.stdin.readline().strip())
answer = {1: 0, 2: 1}
print(solution(N))

