from heapq import heappop, heappush
import sys


def solution():
    check = [[float('inf')] * (M+1) for _ in range(N+1)]
    temp = [(0, 0, 1)]

    while temp:
        d, c, idx = heappop(temp)
        if check[idx][c] < d:
            continue
        if idx == N:
            return d
        for k, l, m in dist[idx]:
            l += c
            m += d
            if M >= l and check[k][l] > m:
                for i in range(l, M+1):
                    if check[k][i] > m:
                        check[k][i] = m
                    else:
                        break
                heappush(temp, (m, l, k))
    return 'Poor KCM'


T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    dist = {i: [] for i in range(N+1)}

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        dist[u].append((v, c, d))

    print(solution())