my_arr = [0] * 10

for i in range(10):
    my_arr[i] = list(map(int, input().split()))

x, y = 1, 1

while True:
    if my_arr[x][y] == 2:
        my_arr[x][y] = 9
        break
    else:
        my_arr[x][y] = 9

        if my_arr[x][y+1] != 1:
            y += 1
        elif my_arr[x+1][y] != 1:
            x += 1
        else:
            break

for i in range(10):
    print(*my_arr[i])

