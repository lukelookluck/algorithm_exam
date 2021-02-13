import sys

n = int(sys.stdin.readline())
my_stack = []
digit = 1
answer = []

for i in range(n):
    key = int(sys.stdin.readline())

    if my_stack and my_stack[-1] == key:
        my_stack.pop()
        answer.append('-')

    else:
        while digit <= n:
            my_stack.append(digit)
            answer.append('+')
            digit += 1

            if my_stack[-1] == key:
                my_stack.pop()
                answer.append('-')
                break

if not my_stack:
    print(*answer, sep='\n')
else:
    print('NO')