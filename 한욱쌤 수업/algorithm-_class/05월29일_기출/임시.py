import sys, time
sys.stdin = open('공통조상.txt')

st = time.time()


def my_func(x):
    global cnt
    for i in my_list2[x]:
        cnt += 1
        if i in my_list2:
            # print(i)
            my_func(i)


T = int(input())
for tc in range(T):
    V, E, FD1, FD2 = map(int, input().split())
    data = [*map(int, input().split())]
    # print(data)
    my_list = {}
    my_list2 = {}
    # print(E)
    for i in range(0, E * 2, 2):
        if data[i + 1] in my_list:
            my_list[data[i + 1]] += data[i]
        else:
            my_list[data[i + 1]] = data[i]
        if data[i] in my_list2:
            my_list2[data[i]] += [data[i + 1]]
        else:
            my_list2[data[i]] = [data[i + 1]]
    temp_list1, temp_list2 = [], []
    # print(my_list)
    # print(my_list2)
    # print(FD1, FD2)
    cnt = 0
    x, y = FD1, FD2
    while cnt != 1:
        if x in my_list:
            temp_list1.append(my_list[x])
            x = my_list[x]
        else:
            break
    while cnt != 1:
        if y in my_list:
            temp_list2.append(my_list[y])
            y = my_list[y]
        # x, y = my_list[x], my_list[y]
        # print(x)
        else:
            break
    my_list1 = []
    # print("#{}".format(tc+1), temp_list1, temp_list2)

    for i in temp_list1[::-1]:
        if i in temp_list2:
            my_list1.append(i)

    # print(my_list1)
    cnt = 0
    my_func(my_list1[-1])
    print("#{}".format(tc + 1), my_list1[-1], cnt + 1)

print(time.time() - st)