import sys
sys.stdin = open('화물 도크.txt')

def my_func(second_digit, my_index):
    global last_digit, result
    last_digit = float('inf')
    used[my_index] = 1
    result += 1
    my_bool = False
    if second_digit == 24:
        return
    for i in range(len(s_list)):
        if used[i] != 1:
            if s_list[i] >= second_digit and e_list[i] < last_digit:
                 last_digit, my_index = e_list[i], i
                 my_bool = True
    # print(used)
    if my_bool is True:
        my_func(last_digit, my_index)





T = int(input())
for tc in range(T):
    N = int(input())
    s_list, e_list = [], []
    used = [*[0]*N]
    for n in range(N):
        s, e = map(int, input().split())
        s_list.append(s)
        e_list.append(e)
    # print(s_list, e_list)
    start_digit = min(e_list)
    start_digit_index = e_list.index(min(e_list))
    # print(e_list.index(14))
    used[start_digit_index] = 1
    # print(used)
    result = 0
    my_func(start_digit, start_digit_index)
    print("#{} {}".format(tc+1, result))
