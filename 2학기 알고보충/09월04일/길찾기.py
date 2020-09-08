from collections import deque


import sys
sys.stdin = open('길찾기.txt')

def my_func():
    global answer

    if answer:
        return

    if my_stack:
        n = my_stack.popleft()
        visited.append(n)

        if n in my_list:
            for i in my_list[n]:
                if i not in visited:
                    my_stack.append(i)
                if i == 99:
                    answer = 1

        my_func()
    else:
        return





T = 10
for tc in range(T):
    a, len = map(int, input().split())
    data = list(map(int, input().split()))
    my_list = {}
    my_stack = deque([0])
    visited = []
    answer = 0

    for i in range(0, len*2, 2):
        if data[i] in my_list:
            my_list[data[i]] += [data[i+1]]
        else:
            my_list[data[i]] = [data[i+1]]

    my_func()
    print("#{} {}".format(tc+1, answer))

