from collections import deque
import sys
sys.stdin = open('2252 줄 세우기.txt')

N, M = map(int, sys.stdin.readline().split())
sequence = [0 for _ in range(N+1)]
result = [[] for _ in range(N+1)]

for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    sequence[B] += 1
    result[A].append(B)

my_q = deque()
for i in range(1, N+1):
    if sequence[i] == 0:
        my_q.append(i)

answer = []

while my_q:
    x = my_q.popleft()
    answer.append(x)
    for i in result[x]:
        sequence[i] -= 1
        if sequence[i] == 0:
            my_q.append(i)

print(*answer)