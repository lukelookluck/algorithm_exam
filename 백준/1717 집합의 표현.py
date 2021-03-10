import sys


def find(x):
    if my_set[x] < 0:
        return x

    my_set[x] = find(my_set[x])
    return my_set[x]


def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return

    if my_set[x] < my_set[y]:
        my_set[x] += my_set[y]
        my_set[y] = x
    else:
        my_set[y] += my_set[x]
        my_set[x] = y


n, m = map(int, sys.stdin.readline().split())
my_set = [-1] * (n + 1)

for _ in range(m):
    key, a, b = map(int, sys.stdin.readline().split())

    if not key:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
