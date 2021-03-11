import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return

    if home[a] < home[b]:
        home[a] += home[b]
        home[b] = a

    else:
        home[b] += home[a]
        home[a] = b


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

home = [-1] * (N + 1)

for i in range(1, N+1):
    for j, value in enumerate(map(int, sys.stdin.readline().split())):
        if value:
            union(i, j+1)

plan = list(map(int, sys.stdin.readline().split()))
answer = 'YES'

for i in range(M-1):
    if find(plan[i]) != find(plan[i+1]):
        answer = 'NO'
        break

print(answer)