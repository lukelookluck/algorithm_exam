import sys, time
sys.stdin = open('하나로.txt')

st = time.time()


def my_func():
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[j][i] = (dx[i] - dx[j]) ** 2 + (dy[i] - dy[j]) ** 2

    values_list = [float('inf') for _ in range(N)]
    values_list[0] = 0
    check_list = [0] * N

    x, cnt = 0, 0
    while cnt != N - 1:
        check_list[x] = 1
        my_min = float('inf')
        temp_idx = None
        for i in range(N):
            if not check_list[i]:
                if values_list[i] > arr[x][i]:
                    values_list[i] = arr[x][i]
                if my_min > values_list[i]:
                    my_min = values_list[i]
                    temp_idx = i
        x = temp_idx
        cnt += 1
    return round(sum(values_list) * E)


T = int(input())
for tc in range(T):
    N = int(input())
    dx = [*map(int, input().split())]
    dy = [*map(int, input().split())]
    E = float(input())
    print("#{} {}".format(tc+1, my_func()))
print(time.time() - st)