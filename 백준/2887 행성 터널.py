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
        if home[a] < home[b]:
            home[a] += home[b]
            home[b] = a
        else:
            home[b] += home[a]
            home[a] = b


N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
home = [-1] * N
my_heap = []
answer, cnt = 0, 0

for i in range(3):
    arr.sort(key=lambda x: x[i])
    for j in range(1, N):
        heappush(my_heap, (abs(arr[j][i] - arr[j-1][i]), arr[j][3], arr[j-1][3]))

for _ in range(len(my_heap)):
    w, a, b = heappop(my_heap)

    if find(a) != find(b):
        union(a, b)
        answer += w
        cnt += 1

        if cnt == N-1:
            break

print(answer)
