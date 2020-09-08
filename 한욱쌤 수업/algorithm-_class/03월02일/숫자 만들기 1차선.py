import sys, math
sys.stdin = open('숫자 만들기.txt')

def permutation(k, n):
    global used
    if k == n:
        # print([[*opt]])
        if opt not in used:
            used += [[*opt]]
        # for i in range(N-1):
        #     result.append(operate(result[i], digits[i], opt[i]))
        # print(result)

    else:
        for i in range(k, n):
            opt[k], opt[i] = opt[i], opt[k]
            permutation(k+1, n)
            opt[k], opt[i] = opt[i], opt[k]

def operate(var1, var2, operator):
    if operator == '+':
        return var1 + var2
    if operator == '-':
        return var1 - var2
    if operator == '*':
        return var1 * var2
    if operator == '/':
        if var1 // var2 < 0:
            return -int(abs(var1 / var2))
        else:
            return int(abs(var1 / var2))

T = int(input())
for tc in range(T):
    N = int(input())
    opt_variable = ['+', '-', '*', '/']
    opt_num = list(map(int, input().split()))
    opt = []
    used = []
    for i in range(4):
        opt += opt_variable[i]*opt_num[i]
    digits = list(map(int, input().split()))
    result = [digits.pop(0)]
    # print("result", result)
    permutation(0, len(opt))
    # print(len(used))
    # print("digits", digits)
    # print("used", used)
    operate_result = []
    my_max = float('-inf')
    my_min = float('inf')
    for u in used:
        result = [result[0]]
        for i in range(N-1):
            result.append(operate(result[i], digits[i], u[i]))
        print(result)
        operate_result.append(result[N-1])

    # ans = max(operate_result) - min(operate_result)
    # print("#{} {}".format(tc+1, ans))