import sys

N, M = map(int, sys.stdin.readline().split())

toCheck = {sys.stdin.readline().strip() for _ in range(N)}

answer = 0

for _ in range(M):
    if sys.stdin.readline().strip() in toCheck:
        answer += 1

print(answer)
