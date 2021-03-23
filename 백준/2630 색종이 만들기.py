import sys


def solution(s_x, e_x, s_y, e_y):
    global b, w

    all_blue, all_white = True, True
    temp_x, temp_y = e_x - s_x, e_y - s_y

    if (temp_x < 1) or (temp_y < 1):
        return

    for i in range(s_x, e_x):
        for j in range(s_y, e_y):
            if arr[i][j] == 0:
                all_blue = False
            else:
                all_white = False

    if all_blue or all_white:
        if all_blue:
            b += 1
        if all_white:
            w += 1
    else:
        solution(s_x, s_x + temp_x // 2, s_y, s_y + temp_y // 2)
        solution(s_x, s_x + temp_x // 2, s_y + temp_y // 2, e_y)
        solution(s_x + temp_x // 2, e_x, s_y, s_y + temp_y // 2)
        solution(s_x + temp_x // 2, e_x, s_y + temp_y // 2, e_y)


N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b, w = 0, 0
solution(0, N, 0, N)
print(w, b, sep='\n')