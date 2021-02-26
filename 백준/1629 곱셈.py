import sys


def solution(x, y):
    if y == 1:
        return x % C

    else:
        result = solution(x, y // 2)
        if y % 2:
            return result * result * x % C
        else:
            return result * result % C


A, B, C = map(int, sys.stdin.readline().split())
print(pow(A, B, C))
print(solution(A, B))


