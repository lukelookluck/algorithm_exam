import sys


def solution():
    check = [float('inf')] * (N + 1)
    check[1] = 0
    for n in range(1, N+1):
        for i in range(1, N+1):
            if check[i] == float('inf'):
                continue
            for k, l in dist[i].items():
                l += check[i]
                if check[k] > l:
                    if n == N:
                        return [-1]
                    check[k] = l

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
