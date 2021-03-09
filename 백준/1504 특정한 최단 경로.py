from heapq import heappush, heappop
import sys


def solution(s):
    check = [float('inf')] * (N + 1)
    check[s] = 0
    temp = [(0, s)]

    while temp:
        x, y = heappop(temp)
        if check[y] >= x:
            for n, m in dist[y]:
                m += x
                if check[n] > m:
                    check[n] = m
                    heappush(temp, (m, n))

    return check


N, E = map(int, sys.stdin.readline().split())
dist = {i: [] for i in range(N + 1)}

for e in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a].append((b, c))
    dist[b].append((a, c))

to_go = [1] + list(map(int, sys.stdin.readline().split()))

result = []

for tg in to_go:
    result.append(solution(tg))

answer = min(result[0][to_go[1]] + result[1][to_go[2]] + result[2][N],
             result[0][to_go[2]] + result[2][to_go[1]] + result[1][N])

print(-1 if answer == float('inf') else answer)

