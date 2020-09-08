import sys, time
sys.stdin = open('최적 경로.txt')

st = time.time()

def my_func(x, y, m):
    global start_idx, end_idx, my_result
    my_min = float('inf')
    my_index = None
    for i in range(0, L, 2):
        my_distance = abs(x - arr[i]) + abs(y - arr[i+1])
        if my_min > my_distance:
            my_min = my_distance
            my_index = i
    print(my_index)
    my_result += my_min
    check_list[my_index // 2] = 1
    if m == 0:
        start_idx = my_index
    else:
        end_idx = my_index


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [*map(int, input().split())]
    st_en = arr[:4]
    arr = arr[4:]
    L = len(arr)
    check_list = [0] * N
    start_idx = None
    end_idx = None
    my_result = 0
    for i in range(0, len(st_en), 2):
        my_func(st_en[i], st_en[i+1], i)
    print(st_en, arr, check_list)
    print(start_idx, end_idx)
    print(0//2)
    cnt = 0
    while cnt != N-2:
        my_min = float('inf')
        my_index = None
        for i in range(0, L, 2):
            my_distance = abs(arr[start_idx] - arr[i]) + abs(arr[start_idx + 1] - arr[i + 1])
            if my_min > my_distance and check_list[i // 2] == 0:
                my_min = my_distance
                my_index = i
        print(my_index)
        my_result += my_min
        check_list[my_index // 2] = 1
        start_idx = my_index
        cnt += 1
    print(st_en, arr, check_list)
    my_result += abs(arr[start_idx] - arr[end_idx]) + abs(arr[start_idx+1] - arr[end_idx+1])
    print(N)
    print("#{}".format(tc+1), my_result)

print(time.time() - st)
