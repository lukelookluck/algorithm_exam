import sys
sys.stdin = open('반복문자 지우기.txt')

def my_func(data):
    my_stack = []
    for i in data:
        my_stack.append(i)

        if i == my_stack[-1]:
            my_stack.pop()
    return my_stack


T = int(input())
for tc in range(T):
    data = str(input())

    # my_stack = []
    # for i in data:
    #     if i not in my_stack:
    #         my_stack.append(i)
    #
    # for i in data:
    #     if i == my_stack[-1]:
    #         my_stack.pop()
    # print(my_stack)

    print(my_func(data))

