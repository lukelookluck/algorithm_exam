import sys, time
sys.stdin = open('최대 상금.txt')

st = time.time()


def my_func(k, l):
    global my_result
    if k == N:
        digit = int(''.join(data))
        if my_result < digit:
            my_result = digit
        return
    else:
        for i in range(l, L):
            for j in range(i + 1, L):
                data[i], data[j] = data[j], data[i]
                my_func(k+1, i)
                data[i], data[j] = data[j], data[i]

T = int(input())
for tc in range(T):
    data_t, N = map(int, input().split())
    data_t = str(data_t)
    L = len(data_t)
    if N > L:
        N = L
    my_result = float('-inf')
    data = [*map(str, data_t)]
    my_func(0, 0)
    print("#{} {}".format(tc+1, my_result))

print(time.time() - st)