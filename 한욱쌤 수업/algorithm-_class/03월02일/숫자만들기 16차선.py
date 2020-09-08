import sys, math
sys.stdin = open('숫자 만들기.txt')

def my_func(p, s, m, d, count, digit):
    global my_max, my_min
    if count == N-1:
        my_max = max(my_max, digit)
        my_min = min(my_min, digit)
        return
    else:
        if p > 0:
            my_func(p-1, s, m, d, count+1, digit + digits[count+1])
        if s > 0:
            my_func(p, s-1, m, d, count+1, digit - digits[count+1])
        if m > 0:
            my_func(p, s, m-1, d, count+1, digit * digits[count+1])
        if d > 0:
            if digit // digits[count+1] < 0:
                return my_func(p, s, m, d-1, count+1, -int(abs(digit / digits[count+1])))
            else:
                return my_func(p, s, m, d-1, count+1, int(abs(digit / digits[count+1])))
                    # int(abs(digit / digits[count+1]))



T = int(input())
for tc in range(T):
    N = int(input())

    p, s, m, d = map(int, input().split())
    opt = []
    used = []
    digits = list(map(int, input().split()))

    my_max = float('-inf')
    my_min = float('inf')
    my_func(p, s, m, d, 0, digits[0])
    # print(len(used))
    # print("digits", digits)
    # print("used", used)
    operate_result = []
    print("#{} {}".format(tc+1, my_max - my_min))