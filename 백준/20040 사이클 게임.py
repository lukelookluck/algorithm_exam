import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b, idx):
    a, b = find(a), find(b)

    if a == b:
        print(idx)
        sys.exit(0)

    if home[a] < home[b]:
        home[a] += home[b]
        home[b] = a
    else:
        home[b] += home[a]
        home[a] = b


n, m = map(int, sys.stdin.readline().split())
home = [-1] * n

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, i)

print(0)