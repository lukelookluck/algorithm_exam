import sys

def solution(x, y, cnt):
    check[x][y] = 1
    for d in range(4):
        new_x, new_y = x + dx[d], y + dy[d]
        if 0 <= new_x < N and 0 <= new_y < N:
            if data[new_x][new_y] == 1 and check[new_x][new_y] == 0:
                cnt += solution(new_x, new_y, 1)

    return cnt



N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
check = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
ans_cnt = 0

for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and check[i][j] == 0:
            ans.append(solution(i, j, 1))
            ans_cnt += 1

ans.sort()
print(ans_cnt, *ans, sep='\n')