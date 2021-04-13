import sys
sys.setrecursionlimit(10 ** 9)


def solution(x, y):
    if x > W or y > W:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]

    nc = max(x, y) + 1
    nx = solution(nc, y) + abs(dist[nc][0] - dist[x][0]) + abs(dist[nc][1] - dist[x][1])
    ny = solution(x, nc) + abs(dist[nc][0] - dist[y][0]) + abs(dist[nc][1] - dist[y][1])
    dp[x][y] = min(nx, ny)

    return dp[x][y]


def route(x, y):
    if x > W or y > W:
        return
    nc = max(x, y) + 1
    nx = abs(dist[nc][0] - dist[x][0]) + abs(dist[nc][1] - dist[x][1])
    ny = abs(dist[nc][0] - dist[y][0]) + abs(dist[nc][1] - dist[y][1])

    if dp[nc][y] + nx < dp[x][nc] + ny:
        print(1)
        route(nc, y)
    else:
        print(2)
        route(x, nc)


N = int(sys.stdin.readline().strip())
W = int(sys.stdin.readline().strip())
dist = [(1, 1), (N, N)]

for _ in range(W):
    dist.append(tuple(map(int, input().split())))

dp = [[-1] * (W+2) for _ in range(W+2)]

print(solution(0, 1))
route(0, 1)