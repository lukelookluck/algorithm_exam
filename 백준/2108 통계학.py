import sys

N = int(sys.stdin.readline())
check = [0] * 8001
my_sum, cnt, my_med = 0, 0, 4001

for n in range(N):
    check[4000 + int(sys.stdin.readline())] += 1

check_max = max(check)
check_max_list = []
my_max, my_min = 0, 4001

for i in range(8001):
    if check[i]:
        my_sum += (i - 4000) * check[i]
        cnt += check[i]
        if check[i] == check_max:
            check_max_list.append(i - 4000)
        if my_med == 4001 and cnt >= N // 2 + 1:
            my_med = i - 4000
        if my_min == 4001:
            my_min = i - 4000
        my_max = i - 4000


print(round(my_sum / N))

print(my_med)

if len(check_max_list) > 1:
    print(check_max_list[1])
else:
    print(check_max_list[0])

print(my_max - my_min)