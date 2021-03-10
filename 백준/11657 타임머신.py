import sys


def solution():
    check = [float('inf')] * (N + 1)
    check[1] = 0
    for _ in range(N):
        for i in range(1, N+1):
            for k, l in dist[i].items():
                l += check[i]
                if check[i] == float('inf'):
                    continue
                if check[k] > l:
                    check[k] = l

    for i in range(1, N+1):
        for k, l in dist[i].items():
            l += check[i]
            if check[i] == float('inf'):
                continue
            if check[k] > l:
                return [-1]

    return check[2:]


N, M = map(int, sys.stdin.readline().split())
dist = {i: {} for i in range(1, N+1)}

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if b in dist[a]:
        dist[a][b] = min(dist[a][b], c)
    else:
        dist[a][b] = c

for ans in solution():
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)