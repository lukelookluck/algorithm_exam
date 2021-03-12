import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    a, b = find(a), find(b)

    if home[a] < home[b]:
        home[a] += home[b]
        home[b] = a
    else:
        home[b] += home[a]
        home[a] = b


V, E = map(int, sys.stdin.readline().split())
home = [-1] * (V + 1)
arr = []
answer, cnt = 0, 0

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([c, a, b])

arr.sort(key=lambda x: x[0])

for i in range(E):
    weight, a, b = arr[i]
    if find(a) != find(b):
        union(a, b)
        answer += weight
        cnt += 1

    if cnt == V-1:
        break

print(answer)
