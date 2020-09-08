import sys, time
st = time.time()
sys.stdin = open('최소 신장 트리.txt')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    key = [-1] * (V + 1)
    value_list = [float('inf')] * (V + 1)
    linked_list = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n1 in linked_list:
            linked_list[n1] += [(n2, w)]
            if n2 in linked_list:
                linked_list[n2] += [(n1, w)]
            else:
                linked_list[n2] = [(n1, w)]
        else:
            linked_list[n1] = [(n2, w)]
            if n2 in linked_list:
                linked_list[n2] += [(n1, w)]
            else:
                linked_list[n2] = [(n1, w)]
    key[0] = 0
    value_list[0] = 0

    # print(key)
    # print(value_list)
    # print(linked_list)

    digit = 0
    digit2 = 0
    cnt = 0
    result = 0
    while cnt != V:
        my_min = float('inf')
        for k in range(V + 1):
            # print("k", k)
            if key[k] != -1:
                # print(k)
                for n2, w in linked_list[k]:
                    # print(n2, w)
                    if key[n2] == -1 and my_min > w:
                        digit = n2
                        my_min = w
                        digit2 = k
                        # print(digit, my_min, digit2)

        key[digit] = digit2
        value_list[digit] = my_min
        result += my_min
        cnt += 1
    # print(key)
    # print(value_list)
    print("#{} {}".format(tc+1, result))

print(time.time() - st)