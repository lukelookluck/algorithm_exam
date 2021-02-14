from collections import deque
import sys

N = int(sys.stdin.readline().strip())
my_deq = deque()

for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push':
        my_deq.append(order[1])

    elif order[0] == 'pop':
        print(my_deq.popleft() if my_deq else -1)

    elif order[0] == 'size':
        print(len(my_deq))

    elif order[0] == 'empty':
        print(0 if my_deq else 1)

    elif order[0] == 'front':
        print(my_deq[0] if my_deq else -1)

    else:
        print(my_deq[-1] if my_deq else -1)