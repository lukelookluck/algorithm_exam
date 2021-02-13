my_arr = [0] * 19

for i in range(19):
    my_arr[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if my_arr[j][y-1] == 0:
            my_arr[j][y-1] = 1
        else:
            my_arr[j][y-1] = 0
    for j in range(19):
        if my_arr[x-1][j] == 0:
            my_arr[x-1][j] = 1
        else:
            my_arr[x-1][j] = 0

for i in range(19):
    print(*my_arr[i])
