import sys
sys.stdin = open('핀볼 게임.txt')


def my_func(i, j, direction):
    global result_cnt
    cnt = 0
    fi, fj = i, j
    m = direction
    while True:
        si = fi + dx[m]
        sj = fj + dy[m]

        if si == i and sj == j:
            break

        if not 0 <= si < N or not 0 <= sj < N:
            cnt += cnt + 1
            break

        if arr[si][sj] == 0:
            fi, fj = si, sj
            continue

        if 1 <= arr[si][sj] <= 4:
            if m == arr[si][sj] % 4:
                m = (m + 1) % 4
                cnt += 1
                fi, fj = si, sj
                continue
            elif m + 1 == arr[si][sj]:
                m = (m + 3) % 4
                cnt += 1
                fi, fj = si, sj
                continue
            else:
                cnt += cnt + 1
                break

        if arr[si][sj] == 5:
            cnt += cnt + 1
            break

        if 6 <= arr[si][sj] <= 10:
            fi, fj = wh(arr[si][sj], si, sj)
            continue

        if arr[si][sj] == -1:
            break

    if result_cnt < cnt:
        result_cnt = cnt


def wh(value, a, b):
    for v, q, w in wormhole_list:
        # print(v, q, w)
        if v == value and (q, w) != (a, b):
            return q, w


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    # print(arr)
    wormhole_list = []
    result_cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                wormhole_list.append((arr[i][j], i, j))
    # print(wormhole_list)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for d in range(4):
                    my_func(i, j, d)

    print("#{} {}".format(tc + 1, result_cnt))
