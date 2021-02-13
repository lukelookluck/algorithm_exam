import sys

N = int(sys.stdin.readline())
my_stack = []

for n in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        my_stack.append(order[1])
    elif order[0] == 'pop':
        if my_stack:
            print(my_stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(my_stack))
    elif order[0] == 'empty':
        if my_stack:
            print(0)
        else:
            print(1)
    else:
        if my_stack:
            print(my_stack[-1])
        else:
            print(-1)

