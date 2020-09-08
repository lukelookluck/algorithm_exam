import sys, time
sys.stdin = open('최소 이동 거리.txt')

st = time.time()

def my_func(num, my_sum):
    global my_min
    if num in linked_list:
        for n, w in linked_list[num]:
            if my_sum > my_min:
                return
            if n == N:
                if my_min > my_sum+w:
                    my_min = my_sum+w
                    # print(result, my_min)
                return
            if key[n] == -1:
                key[num] = 1
                result.append(num)
                my_func(n, my_sum + w)
                key[num] = -1
                result.pop()


T = int(input())
for tc in range(T):
    N, E = map(int, input().split())
    key = [-1] * (N+1)
    linked_list = {}
    my_min = float('inf')
    result = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n1 in linked_list:
            linked_list[n1] += [(n2, w)]
        else:
            linked_list[n1] = [(n2, w)]

    print(linked_list)
    my_func(0, 0)
    print("#{} {}".format(tc+1, my_min))
    # print(result)

print(time.time() - st)