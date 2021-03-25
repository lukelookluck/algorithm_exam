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


# while temp:4 3
# 2 3 1
# 3 4 1
# 4 2 1
#     c, a = heappop(temp)
#     print(c, a)
#     # if
#     if check[a][0] > c:
#         for idx, d in dist[a]:
#             d += c
#             if check[idx][0] == d and idx = a:
#                 check[idx] = (d, a)
#                 heappush(temp, (d, idx))
#     print(check)
#     print(temp)


'''
import sys


V, E = map(int, sys.stdin.readline().split())
inf = float('inf')
arr = [[inf] * (V+1) for _ in range(V+1)]
answer = inf

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a][b] = c

for x in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min((arr[i][j], arr[i][x] + arr[x][j]))

    answer = min(answer, arr[x][x])

print(answer if answer != inf else -1)
'''