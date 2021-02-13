import sys


def solution(n):
    if n > 1:
        return n * solution(n-1)
    else:
        return 1


N = int(sys.stdin.readline())
print(solution(N))