from heapq import heappop, heappush
import sys

def solution():
    check = [[float('inf')] * (M+1) for _ in range(N+1)]
    check[1][1] = 0
    temp = [[0, 0, 1]]

    while temp:
        d, c, idx = heappop(temp)
        for k, l, m in dist[idx]:
            l += c
            m += d
            if M >= l and check[k][l] > m:
                check[k][l] = m
                heappush(temp, [m, l, k])

    return min(check[N])


T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    dist = {i: [] for i in range(N+1)}

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        dist[u].append([v, c, d])

    result = solution()

    if result <= M:
        print(result)
    else:
        print('Poor KCM')