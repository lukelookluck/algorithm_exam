h, w = map(int, input().split())
n = int(input())

my_arr = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for j in range(l):
            my_arr[x-1][y-1+j] = 1
    else:
        for j in range(l):
            my_arr[x - 1 + j][y - 1] = 1

for i in range(h):
    print(*my_arr[i])