import sys
sys.stdin = open('계산기3.txt')

def my_func(data):
    global my_stack
    result = []

    for i in data:
        if i =='(':
            my_stack.append(i)
            continue

        if i in digit:
            if my_stack[-1] == '*':
                result.append(i)
                result.append(my_stack.pop())
                continue
            else:
                result.append(i)
                continue
                                            # 7*3*(6+2)+6+6)
        if i in ort:
            if i == '+':
                if my_stack[-1] == '*':
                    result.append(my_stack.pop())
                if my_stack[-1] == '+':
                    result.append(my_stack.pop())
                #     continue
                my_stack.append(i)
                continue
            elif i == '*':
                # if len(my_stack) == 0:
                #     my_stack.append(i)
                #     continue
                if my_stack[-1] == '*':
                    my_stack.append(i)
                    result.append(my_stack.pop())
                    continue
                else:
                    my_stack.append(i)
                    continue

        if i == ')':
            while my_stack[-1] != '(':
                result.append(my_stack.pop())
            my_stack.pop()
    return "".join(result)


def my_func2(data):
    global my_stack
    result = []

    for i in data:
        if i in digit:
            my_stack.append(i)
        if i in ort:
            if i == '+':
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(a + b)
            if i == '*':
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(a * b)
    return my_stack









T = 10
for tc in range(T):
    L = int(input())
    data = input()
    # data = '(' + data + ')'
    ort = ['+', '*']

    digit = []
    for i in range(1, 10):
        digit.append(str(i))
    # print(data)

    my_stack = []


    data2 = my_func(data)
    # print(data2)
    print("#{} {}".format(tc+1, *my_func2(data2)))
