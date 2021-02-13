import sys

N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
my_stack = [0]
cnt = 1

while cnt != N:
    while my_stack and data[my_stack[-1]] < data[cnt]:
        answer[my_stack.pop()] = data[cnt]

    my_stack.append(cnt)
    cnt += 1

print(*answer)
