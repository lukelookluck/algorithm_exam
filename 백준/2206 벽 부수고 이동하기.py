import sys


def solution():
    my_d = [(0, 0, 1)]
    check[0][0] = 1
    ans = 1

    while my_d:
        temp = []
        for x, y, crush in my_d:

            if x == N-1 and y == M-1:
                return ans

            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < N and 0 <= new_y < M:
                    if arr[new_x][new_y] == 1 and crush == 1:
                        check[new_x][new_y] = 1
                        temp.append((new_x, new_y, 0))
                    elif arr[new_x][new_y] == 0 and check[new_x][new_y] < crush:
                        check[new_x][new_y] = crush
                        temp.append((new_x, new_y, crush))
        my_d = temp
        ans += 1
    return -1


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
check = [[-1]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(solution())