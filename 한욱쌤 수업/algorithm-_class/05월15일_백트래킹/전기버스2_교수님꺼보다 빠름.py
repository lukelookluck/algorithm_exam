import sys, time
sys.stdin = open('전기버스2.txt')
start = time.time()


def my_func(start_index, n, cnt):
    global my_answer
    if start_index == -N:
        my_answer = cnt-1
        return
    result = 0
    # print(start_index - n + 1)
    for i in range(start_index, start_index - n - 1, -1):
        if i >= -N and data[i] >= start_index - i:
            result = i
    # print("data[i] :", data[result])
    # print("result: ", result)
    my_func(result, n, cnt+1)




T = int(input())
for tc in range(T):
    temperate_list = [*map(int, input().split())]
    N = temperate_list[0]
    data = temperate_list[1:] + [0]
    my_answer = 0
    # print(N, data)
    # print(max(data))
    # for i in range(-1, -N, -1):?
        # print(data[i])
    my_func(-1, max(data), 0)
    print("#{} {}".format(tc+1, my_answer))
print(time.time() - start)