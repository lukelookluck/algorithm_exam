from itertools import combinations
import sys
sys.stdin = open('레벨2-1.txt')

N = int(input())
for i in range(N):
    s = input()

    my_stack = []

    for a in s:
        if len(my_stack) == 0 or (my_stack[-1] =='(' and a == '('):
            if a == '(':
                my_stack.append(a)
            else:
                print(False)
                break
        elif my_stack[-1] == '(' and a == ')':
            my_stack.pop()

    if len(my_stack):
        print(False)
    else:
        print(True)
    print('----------')
