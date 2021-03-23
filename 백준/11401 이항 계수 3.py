import sys


def solution(x, y):
    if y == 1:
        return x % key
    elif y % 2:
        return solution(x ** 2 % key, y // 2) * x % key
    else:
        return solution(x ** 2 % key, y // 2)


N, K = map(int, sys.stdin.readline().split())
K = min(K, N-K)

key = 1000000007
answer = 1
temp = 1

for i in range(K):
    answer *= N-i
    answer %= key
    temp *= K-i
    temp %= key

print(solution(temp, key-2) * answer % key)