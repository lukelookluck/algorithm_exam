from heapq import heappush, heappop
import sys


def solution(x):
    check = [100000000] * (n+1)
    check[x] = 0
    my_heap = [(0, x)]

    while my_heap:
        k, l = heappop(my_heap)
        for o, p in dist[l].items():
            p += k
            if check[o] > p:
                check[o] = p
                heappush(my_heap, (p, o))

    return check


T = int(sys.stdin.readline().strip())
for tc in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    dist = {i: {} for i in range(1, n+1)}

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        dist[a][b] = d
        dist[b][a] = d

    s_re = solution(s)
    g_re = solution(g)
    h_re = solution(h)

    answer = []

    for _ in range(t):
        x = int(sys.stdin.readline().strip())
        if s_re[x] != float('inf') and (s_re[x] == s_re[g] + g_re[h] + h_re[x] or s_re[x] == s_re[h] + h_re[g] + g_re[x]):
            answer.append(x)

    print(*sorted(answer))

