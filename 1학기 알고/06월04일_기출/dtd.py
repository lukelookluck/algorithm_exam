import sys, time
from collections import deque
sys.stdin = open('보급로.txt')

st = time.time()

def solve(n, lines):
    visited = [[-1] * n for i in range(n)]
    visited[0][0] = lines[0][0]
    Q = deque()
    Q.append((0, 0))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while Q:
        x, y = Q.popleft()
        if x == n - 1 and y == n - 1:
            continue
        current_v = visited[x][y]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
                continue

            if visited[temp_x][temp_y] == -1 or current_v + lines[temp_x][temp_y] < visited[temp_x][temp_y]:
                visited[temp_x][temp_y] = current_v + lines[temp_x][temp_y]
                Q.append((temp_x, temp_y))

    return visited[n - 1][n - 1]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lines = [[*map(int, input())] for _ in range(n)]
    ans = solve(n, lines)

    # visited = [[-1] * n for i in range(n)]
    # Q = deque()
    # Q.append((0, 0))
    # visited[0][0] = lines[0][0]
    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    # while Q:
    #     x, y = Q.popleft()
    #     if x == n - 1 and y == n - 1:
    #         continue
    #     current_v = visited[x][y]
    #     for i in range(4):
    #         temp_x = x + dx[i]
    #         temp_y = y + dy[i]
    #
    #         if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
    #             continue
    #
    #         if visited[temp_x][temp_y] == -1 or current_v + lines[temp_x][temp_y] < visited[temp_x][temp_y]:
    #             visited[temp_x][temp_y] = current_v + lines[temp_x][temp_y]
    #             Q.append((temp_x, temp_y))
    # ans = visited[n - 1][n - 1]

    print("#{} {}".format(tc, ans))
print(time.time() - st)