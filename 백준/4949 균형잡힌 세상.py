import sys

while True:
    data = sys.stdin.readline().rstrip()
    print(data)

    if data == '.':
        break

    my_stack = []

    for dt in data:
        if dt == '(':
            my_stack.append(dt)

        elif dt == ')':
            if my_stack and my_stack[-1] == '(':
                my_stack.pop()
            else:
                my_stack.append(-1)
                break

        elif dt == '[':
            my_stack.append(dt)

        elif dt == ']':
            if my_stack and my_stack[-1] == '[':
                my_stack.pop()
            else:
                my_stack.append(-1)
                break

    if not my_stack:
        print('yes')
    else:
        print('no')




