import sys
sys.stdin = open('수영장.txt')

def my_func(d, m, q, y, i, my_sum):
    global year_plan, my_min
    if i >= cnt:
        # print(d, m, q, y, my_sum)
        if my_min > my_sum:
            my_min = my_sum
        return
    else:
        my_func(d+1, m, q, y, i+1, my_sum+(dp*my_plan[i]))
        my_func(d, m+1, q, y, i+1, my_sum+mp)
        my_func(d, m, q+1, y, i+3, my_sum+qp)
        my_func(d, m, q, y+1, i+12, my_sum+yp)

T = int(input())
for tc in range(T):
    dp, mp, qp, yp = map(int, input().split())
    pay_list = [dp, mp, qp, yp]
    year_plan = list(map(int, input().split()))
    my_plan= []
    for i in year_plan:
        if i != 0:
            my_plan.append(i)
    cnt = len(my_plan)
    # print(my_plan)
    # chosen_list = [0] * cnt
    # print(chosen_list)
    my_min = float('inf')
    my_func(0, 0, 0, 0, 0, 0)
    print("#{} {}".format(tc+1, my_min))
