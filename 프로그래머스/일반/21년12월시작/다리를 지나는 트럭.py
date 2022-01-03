from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    my_dq = deque([0] * bridge_length)
    my_tr = deque(truck_weights)
    my_sum = 0

    while my_dq:
        answer += 1
        my_sum -= my_dq.popleft()

        if my_tr:
            if my_sum + my_tr[0] <= weight:
                my_sum += my_tr[0]
                my_dq.append(my_tr.popleft())
            else:
                my_dq.append(0)

    return answer
