from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
dist = {i: {} for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if b not in dist[a]:
        dist[a][b] = c
    else:
        dist[a][b] = min(dist[a][b], c)

x, y = map(int, sys.stdin.readline().split())
temp = []
heappush(temp, (0, x))
check = [float('inf')] * (n+1)
cnt = 0

while temp:
    weight, idx = heappop(temp)
    if check[idx] >= weight:
        for toidx, toweight in dist[idx].items():
            toweight += weight
            if check[toidx] > toweight:
                check[toidx] = toweight
                heappush(temp, (toweight, toidx))

    cnt += 1
    if cnt == n:
        break

print(check[y])
