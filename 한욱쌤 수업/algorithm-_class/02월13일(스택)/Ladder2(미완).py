import sys
sys.stdin = open('Ladder2.txt')

import copy

def my_func(x, y, t, count):
    if y == 3:
        return count

    else:
        arr[y][x] = 0
        if y + dy[t] == 4 or x + dx[t] == 4:
            t += 1
            if t == 3:
                t = 0


        if arr[y + dy[t]][x + dx[t]] != 1:
            t += 1
            if t == 3:
                t = 0



        else:
            x += dx[t]
            y += dy[t]
            count += 1

        return my_func(x, y, t, count)




T = 10
count = 0
for tc in range(T):
    N = int(input())
    arr1 = [list(map(int, input().split())) for _ in range(4)]
    print(arr1)
    result = []
    dx = [0, 1, -1]
    dy = [1, 0, 0]
    start_list = []

    for i in range(4):
        if arr1[0][i] == 1:
            start_list.append(i)

    for x in start_list:
        arr = copy.deepcopy(arr1)
        y = 0
        result.append(my_func(x, y, 0, 0))

    print(result)



