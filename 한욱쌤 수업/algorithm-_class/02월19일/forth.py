import sys
sys.stdin = open('forth.txt')

def my_func():
    count = 0
    for i in ort:
        for j in data:
            if i == j:
                count += 1

    if len(data) - count - 1 == count + 1:
        my_stack = []
        for i in data:
            a, b = 0, 0
            if i not in ort:
                my_stack.append(i)
            if i in ort:
                if len(my_stack) < 2:
                    return 'error'
                else:
                    a = int(my_stack.pop())
                    b = int(my_stack.pop())

                    if i == '+':
                        my_stack.append(b + a)
                    if i == '-':
                        my_stack.append(b - a)
                    if i == '*':
                        my_stack.append(b * a)
                    if i == '/':
                        my_stack.append(int(b / a))
            if i == '.':
                return my_stack[0]
    else:
        return 'error'


T = int(input())
ort = ['+', '-', '/', '*']

for tc in range(T):

    data = input().split()

    print("#{} {}".format(tc+1, my_func()))