import sys
sys.stdin = open('괄호 변환.txt')


def solution(p):
    if p == '':
        return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:
            r = False
        if c == 0:
            print(r)
            if r:
                print(p[:i+1], p[i+1:])
                return p[:i+1]+solution(p[i+1:])
            else:
                print(p[:i + 1], p[i + 1:])
                # print('a', '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) )))
                print('p[1:i]', p[1:i])
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


T = int(input())
for tc in range(T):
    p = input()
    result = ''

    # solution(p)
    print(solution(p))
    print('-------------')
