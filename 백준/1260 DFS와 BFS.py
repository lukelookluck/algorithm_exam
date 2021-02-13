import sys
from collections import deque


def solution_DFS(idx):
    check[idx] = 1
    print(idx, end=' ')

    for dt in sorted(data[idx]):
        if not check[dt]:
            solution_DFS(dt)


def solution_BFS(V):
    check_BFS = [0] * (N + 1)
    ans = deque()
    ans.append(V)
    check_BFS[V] = 1

    while ans:
        idx = ans.popleft()
        print(idx, end=' ')
        for dt in sorted(data[idx]):
            if not check_BFS[dt]:
                check_BFS[dt] = 1
                ans.append(dt)


N, M, V = map(int, sys.stdin.readline().split())
data = [[] for _ in range(N+1)]
check = [0] * (N+1)

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

solution_DFS(V)
print()
solution_BFS(V)


