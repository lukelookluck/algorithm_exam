from collections import deque
import sys

N = int(sys.stdin.readline().strip())
my_d = deque()

for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push_back':
        my_d.append(order[1])
    elif order[0] == 'push_front':
        my_d.appendleft(order[1])
    elif order[0] == 'pop_front':
        print(my_d.popleft() if my_d else -1)
    elif order[0] == 'pop_back':
        print(my_d.pop() if my_d else -1)
    elif order[0] == 'size':
        print(len(my_d))
    elif order[0] == 'empty':
        print(0 if my_d else 1)
    elif order[0] == 'front':
        print(my_d[0] if my_d else -1)
    else:
        print(my_d[-1] if my_d else -1)