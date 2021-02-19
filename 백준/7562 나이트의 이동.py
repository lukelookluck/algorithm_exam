import sys


def solution(I, start_x, start_y, end_x, end_y):
    to_go = [(start_x, start_y)]
    check[start_x][start_y] = 1
    ans = 0

    while to_go:
        temp = []
        for toX, toY in to_go:
            if toX == end_x and toY == end_y:
                return ans

            for i in range(8):
                new_x, new_y = toX + dx[i], toY + dy[i]
                if 0 <= new_x < I and 0 <= new_y < I:
                    if check[new_x][new_y] == 0:
                        temp.append((new_x, new_y))
                        check[new_x][new_y] = 1

        ans += 1
        to_go = temp
    return ans


T = int(sys.stdin.readline().strip())
for tc in range(T):
    I = int(sys.stdin.readline().strip())
    check = [[0] * I for _ in range(I)]
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]

    print(solution(I, start_x, start_y, end_x, end_y))