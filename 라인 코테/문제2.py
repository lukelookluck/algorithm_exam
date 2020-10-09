from collections import deque

def solution(ball, order):
    answer = []
    my_stack = deque()
    ball = deque(ball)

    for o in order:
        print(o)
        if o == ball[0]:
            answer.append(ball.popleft())
        elif o == ball[-1]:
            answer.append(ball.pop())
        else:
            my_stack.append(o)
        print(ball, my_stack)

        if len(my_stack):
            n = 0
            while n < len(my_stack):
                o = my_stack.popleft()
                print(o)
                if o == ball[0]:
                    answer.append(ball.popleft())
                    n = 0
                elif o == ball[-1]:
                    answer.append(ball.pop())
                    n = 0
                else:
                    my_stack.append(o)
                    n += 1
        print(ball, my_stack)
    print(answer)
    return answer


ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]
solution(ball, order)