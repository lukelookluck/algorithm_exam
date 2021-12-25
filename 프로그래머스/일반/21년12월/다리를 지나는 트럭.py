from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    my_dq = deque([0] * bridge_length)

    while my_dq:
        answer += 1
        my_dq.popleft()

        if truck_weights:
            if sum(my_dq) + truck_weights[0] <= weight:
                my_dq.append(truck_weights.pop(0))
            else:
                my_dq.append(0)

    return answer
