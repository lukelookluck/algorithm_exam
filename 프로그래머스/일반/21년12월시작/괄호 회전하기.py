def solution(s):
    answer = 0

    def search(x):
        my_stack = []
        x = x[:]
        print('x', x)
        my_stack.append(x.pop())
        while x:
            t = x.pop()
            if not my_stack:
                my_stack.append(t)
            elif (my_stack[-1] == ']' and t == '[') or (my_stack[-1] == '}' and t == '{') or (my_stack[-1] == ')' and t == '('):
                my_stack.pop()
            else:
                my_stack.append(t)

            print(my_stack, x)

        if not my_stack:
            nonlocal answer
            answer += 1





    s = list(s)
    for i in range(len(s)):
        search(s)
        s.append(s.pop(0))


    print(answer)
    return answer


s = "}}}"
solution(s)