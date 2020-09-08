import sys
sys.stdin = open('자물쇠와 열쇠.txt')


def rotate(arr):
    n = len(arr)
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_arr[j][n - 1 - i] = arr[i][j]

    return new_arr


def check(k_x, k_y, key, lock, t_size, start, end):
    t_arr = [[0] * t_size for _ in range(t_size)]

    for i in range(len(key)):
        for j in range(len(key)):
            t_arr[k_x + i][k_y + j] = key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            t_arr[i][j] += lock[i - start][j - start]
            if t_arr[i][j] != 1:
                return False
    return True


T = int(input())
for tc in range(T):
    key = [list(map(int, input().split())) for _ in range(3)]
    lock = [list(map(int, input().split())) for _ in range(3)]
    answer = False
    print(key, lock)

    start = len(key) - 1
    end = start + len(lock)
    t_size = start + end

    for i in range(4):
        for j in range(end):
            for k in range(end):
                if check(j, k, key, lock, t_size, start, end):
                    answer = True
        key = rotate(key)

    print(answer)
