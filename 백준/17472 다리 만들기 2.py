import sys


def search_land(x, y, cnt):
    for k in range(4):
        n_x, n_y = x + dx[k], y + dy[k]
        if 0 <= n_x < N and 0 <= n_y < M:
            if arr[n_x][n_y] == 1 and check[n_x][n_y] == 0:
                check[n_x][n_y] = 1
                dist.append((n_x, n_y, cnt))
                search_land(n_x, n_y, cnt)


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


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
dist, data = [], []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and check[i][j] == 0:
            dist.append((i, j, cnt))
            search_land(i, j, cnt)
            cnt += 1

home = [-1] * (cnt + 1)

for i in range(2):
    temp = sorted(dist, key=lambda x: (x[i], x[1-i]))
    for j in range(1, len(temp)):
        if temp[j][i] == temp[j-1][i]:
            if abs(temp[j][1-i] - temp[j-1][1-i]) >= 3:
                data.append((abs(temp[j][1-i] - temp[j-1][1-i]), temp[j][2], temp[j-1][2]))

data.sort(key=lambda x: x[0])
answer, my_cnt = 0, 0

for i in range(len(data)):
    w, a, b = data[i]
    if a == b:
        union(a, b)
    if find(a) != find(b):
        union(a, b)
        answer += w - 1
        my_cnt += 1


print(-1 if not answer or my_cnt != cnt - 1 else answer)
