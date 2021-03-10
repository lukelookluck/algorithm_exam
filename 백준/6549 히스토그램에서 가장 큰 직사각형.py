import sys

while True:
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]

    if n == 0:
        break

    arr = data[1:]
    stack = []
    my_max = 0

    for idx, value in enumerate(arr):
        my_idx = idx
        while stack and stack[-1][0] >= value:
            h, my_idx = stack.pop()
            my_max = max(my_max, (idx - my_idx) * h)

        stack.append((value, my_idx))

    for h, idx in stack:
        my_max = max(my_max, (n - idx) * h)

    print(my_max)