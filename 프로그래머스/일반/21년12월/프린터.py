from collections import deque


def solution(priorities, location):
    answer = 0
    my_dq = deque(priorities)
    order = location + 1

    my_max = max(my_dq)
    print(my_dq)
    while len(my_dq) >= 1:
        x = my_dq.popleft()
        print("my_max", my_max)
        print("my_x", x)
        print("order", order)
        print(answer)

        if x == my_max:
            answer += 1
            if order == 1:
                print("123123")
                return answer
            else:
                order -= 1
            my_max = max(my_dq)
        else:
            my_dq.append(x)
            if order == 1:
                order = len(my_dq)
            else:
                order -= 1

        print(my_dq)




    return answer

a = [1, 1, 9, 1, 1, 1]
b = 0

print(solution(a, b))