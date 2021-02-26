import sys

N, K = map(int, sys.stdin.readline().split())
answer = 1

for i in range(N, N-K, -1):
    answer *= i
    answer /= N+1 - i

print(int(answer))
