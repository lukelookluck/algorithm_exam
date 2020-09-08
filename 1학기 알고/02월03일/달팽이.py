import sys
sys.stdin = open('달팽이.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]
    a, b, i, j = 0, 0, 1, 0

    # for i in range(n * n + 1):
    #     arr[a][b] = i

    while i < N * N + 1:
        arr[a][b] = i
        # my_a = a + direction_x[j]
        # my_b = b + direction_y[j]
        # if my_a > N-1 or my_b > N-1 or arr[my_a][my_b] != 0:
        if a + direction_x[j] > N - 1 or b + direction_y[j] > N - 1 or arr[a + direction_x[j]][b + direction_y[j]] != 0:
            j += 1
            if j == 4:
                j = 0

        a += direction_x[j]
        b += direction_y[j]
        i += 1

    print("#{}".format(tc+1))
    for i in arr:
        print(*i)