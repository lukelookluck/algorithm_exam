from itertools import permutations
from collections import deque


def solution(expression):
    answer = []
    temp = ''
    my_stack = deque()

    def cal(x, y, z):
        if z == '*':
            return int(x) * int(y)
        elif z == '+':
            return int(x) + int(y)
        else:
            return int(x) - int(y)

    def proceed(array, comb):
        array2 = deque(array)
        for c in comb:
            t_a = deque()
            while array2:
                x = array2.popleft()
                if x == c:
                    t_a.append(cal(t_a.pop(), array2.popleft(), c))
                else:
                    t_a.append(x)
            array2 = t_a
        return abs(int(array2[0]))

    for ex in expression:
        if ex.isdigit():
            temp += ex
        else:
            my_stack.append(temp)
            my_stack.append(ex)
            temp = ''
    my_stack.append(temp)

    for combi in permutations(['*', '-', '+']):
        answer.append(proceed(my_stack, combi))

    return max(answer)