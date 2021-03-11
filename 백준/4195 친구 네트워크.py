import sys


def find(x):
    if x == home[x]:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        cnt[b] += cnt[a]
        home[a] = b


T = int(sys.stdin.readline().strip())
for tc in range(T):
    F = int(sys.stdin.readline().strip())
    home = {}
    cnt = {}

    for f in range(F):
        a, b = sys.stdin.readline().split()
        if a not in home:
            home[a] = a
            cnt[a] = -1

        if b not in home:
            home[b] = b
            cnt[b] = -1

        union(a, b)
        print(abs(cnt[find(b)]))
