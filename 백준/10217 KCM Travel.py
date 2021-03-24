from heapq import heappop, heappush
import sys


def solution():
    N, M, K = map(int, sys.stdin.readline().split())
    dist = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        dist[u].append((v, c, d))
    check = [[sys.maxsize] * (M+1) for _ in range(N+1)]
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
            if M < l or check[k][l] <= m:
                continue
            for i in range(l, M+1):
                if check[k][i] > m:
                    check[k][i] = m
                else:
                    break
            heappush(temp, (m, l, k))

    return "Poor KCM"


T = int(sys.stdin.readline().strip())
for tc in range(T):
    print(solution())