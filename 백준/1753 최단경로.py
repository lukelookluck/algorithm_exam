from heapq import heappush, heappop
import sys


def solution():
    while my_heap:
        my_x, my_y = heappop(my_heap)
        if check[my_y] >= my_x:
            for k, l in dist[my_y].items():
                l += my_x
                if check[k] > l:
                    check[k] = l
                    heappush(my_heap, [l, k])


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())
check = [float('inf')] * (V + 1)
my_heap = []
dist = [{} for _ in range(V+1)]
adj = [{} for _ in range(V+1)]


heappush(my_heap, [0, start])
check[start] = 0

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    if b in dist[a]:
        dist[a][b] = min(c, dist[a][b])
    else:
        dist[a][b] = c

solution()

for i in check[1:]:
    print('INF' if i == float('inf') else i)
