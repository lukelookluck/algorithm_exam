import sys

# 섬 크기 탐색 함수, 그 섬의 인덱스와 해당 좌표를 같이 저장
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
    # 빠른 탐색을 위해 최솟값에 저장
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
# cnt = 모든 섬의 개수
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
    	# 같은 행 또는 같은 열의 값만 비교
        if temp[j][i] == temp[j-1][i]:
            if abs(temp[j][1-i] - temp[j-1][1-i]) >= 3:
            	# 섬간 거리가 3이상일 경우, 그 거리와 해당 섬들의 인덱스를 저장
                data.append((abs(temp[j][1-i] - temp[j-1][1-i]), temp[j][2], temp[j-1][2]))

# 섬간 거리를 기준으로 오름차순 정렬
data.sort(key=lambda x: x[0])
answer, my_cnt = 0, 0

for i in range(len(data)):
    w, a, b = data[i]
    # 그 섬들이 서로다른 섬일 경우, 연결하고 가중치 저장
    if find(a) != find(b):
        union(a, b)
        answer += w - 1
        my_cnt += 1

print(-1 if not answer or my_cnt != cnt - 1 else answer)
