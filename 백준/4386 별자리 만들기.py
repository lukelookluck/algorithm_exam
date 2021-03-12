from heapq import heappop, heappush
import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    home[b] = a


n = int(sys.stdin.readline().strip())
arr = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
home = [-1] * (n + 1)

my_heap = []
answer = 0
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        w, a, b = round(pow(pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2), 0.5), 2), i, j
        heappush(my_heap, [w, a, b])

for i in range(len(my_heap)):
    w, a, b = heappop(my_heap)
    f_a, f_b = find(a), find(b)
    if f_a != f_b:
        union(f_a, f_b)
        answer += w
        cnt += 1

        if cnt == n-1:
            break

print(answer)