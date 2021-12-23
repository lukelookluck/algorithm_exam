from collections import deque


def solution(priorities, location):
    answer = 0
    my_dq = deque(priorities)
    order = location

    my_max = max(my_dq)

    while len(my_dq) >= 1:
        x = my_dq.popleft()

        if x == my_max:
            answer += 1
            if order == 0:
                return answer
            else:
                order -= 1
            my_max = max(my_dq)
        else:
            my_dq.append(x)
            if order == 0:
                order = len(my_dq) - 1
            else:
                order -= 1

    return answer