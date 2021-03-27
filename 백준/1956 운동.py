from heapq import heappush, heappop
import sys


def solution(x):
    check = [inf] * (V + 1)
    temp = [(0, x)]

    while temp:
        w, idx = heappop(temp)
        if x == idx and w != 0:
            break
        if check[idx] >= w:
            for i, d in dist[idx]:
                d += w
                if check[i] > d:
                    check[i] = d
                    heappush(temp, (d, i))

    return check[x]


V, E = map(int, sys.stdin.readline().split())
inf = float('inf')
dist = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a].append((b, c))

answer = inf

for x in dist.keys():
    if len(dist[x]):
        answer = min(answer, solution(x))

print(answer if answer != inf else -1)