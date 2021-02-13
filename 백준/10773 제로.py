import sys

K = int(sys.stdin.readline())
my_stack = []
for k in range(K):
    data = int(sys.stdin.readline())
    if data != 0:
        my_stack.append(data)
    else:
        my_stack.pop()

print(sum(my_stack))