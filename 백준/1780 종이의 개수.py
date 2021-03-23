import sys


def solution(s_x, e_x, s_y, e_y):
    global m, z, p

    all_same = True

    if e_x - s_x > 1 and e_y - s_y > 1:
        for i in range(s_x, e_x):
            for j in range(s_y, e_y):
                if arr[i][j] != arr[s_x][s_y]:
                    all_same = False

                if not all_same:
                    temp_x, temp_y = (e_x - s_x) // 3, (e_y - s_y) // 3

                    solution(s_x, s_x + temp_x, s_y, s_y + temp_y)
                    solution(s_x, s_x + temp_x, s_y + temp_y, e_y - temp_y)
                    solution(s_x, s_x + temp_x, e_y - temp_y, e_y)

                    solution(s_x + temp_x, e_x - temp_x, s_y, s_y + temp_y)
                    solution(s_x + temp_x, e_x - temp_x, s_y + temp_y, e_y - temp_y)
                    solution(s_x + temp_x, e_x - temp_x, e_y - temp_y, e_y)

                    solution(e_x - temp_x, e_x, s_y, s_y + temp_y)
                    solution(e_x - temp_x, e_x, s_y + temp_y, e_y - temp_y)
                    solution(e_x - temp_x, e_x, e_y - temp_y, e_y)
                    return

    if arr[s_x][s_y] == -1:
        m += 1
    elif arr[s_x][s_y] == 0:
        z += 1
    else:
        p += 1


N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
m, z, p = 0, 0, 0
solution(0, N, 0, N)
print(m, z, p, sep='\n')