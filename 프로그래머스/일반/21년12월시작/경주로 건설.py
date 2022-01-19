from collections import deque

def solution(board):
    answer = 0
    my_d = deque()
    my_d.append([0, 0, 0, 0])
    len1, len2 = len(board), len(board[0])
    inf = float('inf')
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    check = [[[inf, inf, inf, inf] for _ in range(len2)] for _ in range(len1)]
    check[0][0][0] = 0
    check[0][0][1] = 0
    check[0][0][2] = 0
    check[0][0][3] = 0

    while my_d:
        x, y, direc, cost = my_d.popleft()
        print(*check, sep='\n')
        print()
        for i in range(4):
            n_x, n_y = x + d[i][0], y + d[i][1]

            if not 0 <= n_x < len1 or not 0 <= n_y < len2:
                continue
            if x == 0 and y == 0:
                n_cost = cost + 100
            else:
                if direc == i:
                    n_cost = cost + 100
                else:
                    n_cost = cost + 600

            if not board[n_x][n_y] and check[n_x][n_y][i] > n_cost:
                my_d.append([n_x, n_y, i, n_cost])
                check[n_x][n_y][i] = n_cost
                print(my_d)
    print(check[-1][-1])

    return answer


b = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0]]
solution(b)





