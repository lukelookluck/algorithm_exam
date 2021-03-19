from heapq import heappop, heappush
import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        home[b] = a


N, M = map(int, sys.stdin.readline().split())
home = [-1] * (N + 1)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
my_heap = []
answer, cnt = 0, 0

for i in range(N):
    for j in range(i+1, N):
        weight = pow(pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2), 0.5)
        heappush(my_heap, [weight, i+1, j+1])

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if find(x) != find(y):
        union(x, y)
        cnt += 1

for i in range(len(my_heap)):
    w, a, b = heappop(my_heap)

    if find(a) != find(b):
        union(a, b)
        answer += w
        cnt += 1

        if cnt == N-1:
            break

print(format(round(answer, 2), ".2f"))