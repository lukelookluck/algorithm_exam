import sys


def solution(s_x, e_x, s_y, e_y):
    temp_x, temp_y = e_x - s_x, e_y - s_y
    all_b, all_w = True, True

    if temp_x < 1 or temp_y < 1:
        return

    for i in range(s_x, e_x):
        for j in range(s_y, e_y):
            if arr[i][j] == 0:
                all_b = False
            else:
                all_w = False

    if all_b or all_w:
        if all_b:
            print(1, end='')
        if all_w:
            print(0, end='')
    else:
        print('(', end='')
        solution(s_x, s_x + temp_x // 2, s_y, s_y + temp_y // 2)
        solution(s_x, s_x + temp_x // 2, s_y + temp_y // 2, e_y)
        solution(s_x + temp_x // 2, e_x, s_y, s_y + temp_y // 2)
        solution(s_x + temp_x // 2, e_x, s_y + temp_y // 2, e_y)
        print(')', end='')


N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
solution(0, N, 0, N)