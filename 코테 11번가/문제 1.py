
def solution(S):
    len_S = len(S)
    my_stack = 'aa'

    a_cnt = 0
    for s in S:
        if s == 'a':
            a_cnt += 1
        if a_cnt >= 3:
            return -1
        if s != 'a':
            a_cnt = 0
            my_stack += s
            my_stack += 'aa'
    return len(my_stack)-len_S





T = 1
for tc in range(T):
    S = 'dog'

    print(solution(S))