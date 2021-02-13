import sys, heapq

N, M = map(int, sys.stdin.readline().split())
priority = [[] for _ in range(N+1)]
sequence = [0 for _ in range(N+1)]
eck = [0 for _ in range(N+1)]
for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    priority[A].append(B)
    sequence[B] += 1

my_q = []
cnt = 0
for i in range(1, N+1):
    if sequence[i] == 0:
        heapq.heappush(my_q, i)
# my_q.sort()
answer = []

while my_q:
    x = heapq.heappop(my_q)
    answer.append(x)
    for i in priority[x]:
        sequence[i] -= 1
        if sequence[i] == 0:
            heapq.heappush(my_q, i)
    cnt += 1

print(*answer)
