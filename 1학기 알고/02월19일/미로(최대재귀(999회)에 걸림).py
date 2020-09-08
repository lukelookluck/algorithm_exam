import sys
sys.stdin = open('미로.txt')

# import sys
# sys.setrecursionlimit(10000)

def my_func(start_x, start_y):
    global N, result
    arr[start_x][start_y] = 1


    for i in range(4):
        if (0 <= start_x + dx[i] < N and 0 <= start_y + dy[i] < N):
            if arr[start_x + dx[i]][start_y + dy[i]] == 3:
                result = 1
                return

            if arr[start_x + dx[i]][start_y + dy[i]] == 0:
                x_stack.append(start_x + dx[i])
                y_stack.append(start_y + dy[i])
                # my_func(start_x + dx[i], start_y + dy[i])
    if len(x_stack) != 0:

        return my_func(x_stack.pop(), y_stack.pop())

    else:
        return 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x_stack = []
    y_stack = []

    # print(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x, start_y = i, j

    my_func(start_x, start_y)
    print("#{} {}".format(tc + 1, result))