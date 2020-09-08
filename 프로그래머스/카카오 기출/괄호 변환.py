import sys
sys.stdin = open('괄호 변환.txt')


def solution(p):
    result = ''
    u = ''
    v = ''

    if len(p) == 0 or iscorrect(p):
        return p

    for i in range(2, len(p)+1, 2):
        print(i)
        if isbalance(p[0:i]):
            u = p[:i]
            v = p[i:]
            print('u', u, 'v', v)
            break

    if iscorrect(u):
        result += u + solution(v)
    else:
        result += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(':
                result += ')'
            else:
                result += '('

    return result


def isbalance(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False


def iscorrect(p):
    my_stack = []
    print('my_func2', p)

    for i in range(len(p)):
        if len(my_stack) == 0 or my_stack[-1] == ')' or (my_stack[-1] == '(' and p[i] == '('):
            my_stack.append(p[i])
        elif my_stack[-1] == '(' and p[i] == ')':
            my_stack.pop()
    if len(my_stack) == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(T):
    p = input()
    result = ''

    # solution(p)
    print(solution(p))
    print('-------------')
