from heapq import heappush, heappop
import sys


def solution():
    while my_heap:
        my_x, my_y = heappop(my_heap)
        for k, l in dist[my_x]:
            my_min = my_y + l
            if check[k] > my_min:
                check[k] = my_min
                heappush(my_heap, [k, my_min])


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())
check = [float('inf')] * (V + 1)
my_heap = []
dist = [[] for _ in range(V+1)]

heappush(my_heap, [start, 0])
check[start] = 0

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a].append([b, c])

solution()

for i in check[1:]:
    print('INF' if i == float('inf') else i)
