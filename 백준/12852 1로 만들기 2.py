from collections import deque
import sys


def solution1(N):
    temp = deque([[N]])
    while temp:
        x_list = temp.popleft()
        x = x_list[-1]
        if x == 1:
            print(len(x_list) - 1)
            print(*x_list)
            sys.exit(0)

        if not x % 3 and check[x // 3] == -1:
            temp.append(x_list + [x // 3])
        if not x % 2 and check[x // 2] == -1:
            temp.append(x_list + [x // 2])
        if check[x - 1] == -1:
            temp.append(x_list + [x - 1])


N = int(sys.stdin.readline().strip())
check = [-1] * (N+1)
solution1(N)
