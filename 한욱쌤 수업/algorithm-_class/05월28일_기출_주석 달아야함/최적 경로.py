import sys, time
sys.stdin = open('최적 경로.txt')

st = time.time()


def my_func(x, y, m, cnt):
    global my_min, my_result
    if m >= my_min:
        return
    if cnt == N:
        m += abs(x - st_en[2]) + abs(y - st_en[3])
        if my_min > m:
            my_min = m
        return
    for i in range(0, L, 2):
        # my_distance = abs(x - arr[i]) + abs(y - arr[i+1])
        if check_list[i // 2] != 1:
            check_list[i // 2] = 1
            my_func(arr[i], arr[i + 1], m + abs(x - arr[i]) + abs(y - arr[i+1]), cnt + 1)
            check_list[i // 2] = 0


def my_func2(x, y):
    my_result1 = 0
    check_list1 = [0] * N
    my_index = None
    cnt = 0
    while cnt != N:
        my_min1 = float('inf')
        for i in range(0, L, 2):
            # print(x, y)
            my_distance = abs(x - arr[i]) + abs(y - arr[i + 1])
            # print(my_distance)
            if my_min1 > my_distance and check_list1[i // 2] == 0:
                my_min1 = my_distance
                # print("my_min1", my_min1)
                my_index = i
        my_result1 += my_min1
        check_list1[my_index // 2] = 1
        x = arr[my_index]
        y = arr[my_index + 1]
        # print(x, y)
        cnt += 1
        # print(check_list1)
        # print(my_result1)
    my_result1 += abs(x - st_en[2]) + abs(y - st_en[3])
    return my_result1


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [*map(int, input().split())]
    st_en = arr[:4]
    arr = arr[4:]
    # print(arr)
    L = len(arr)
    check_list = [0] * N
    # print(my_func2(st_en[0], st_en[1]))
    my_min = my_func2(st_en[0], st_en[1])
    my_result = 0
    st_idx, en_idx = 0, 0
    # break
    my_func(st_en[0], st_en[1], 0, 0)

    print("#{}".format(tc+1), my_min)


print(time.time() - st)
