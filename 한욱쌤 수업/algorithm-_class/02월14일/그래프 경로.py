import sys
sys.stdin = open('그래프 경로.txt')


def my_func(arr, find_r):
    my_stack = [find_r]
    my_visited = []
    while my_stack:
        factor = my_stack.pop()
        my_visited.append(factor)
        for j in range(V):
            # print(factor)
            if arr[factor][j] == 1 and j not in my_stack+my_visited:
                my_stack.append(j)
        if find_c in my_stack:
            return 1
    return 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0 for _ in range(V)] for _ in range(V)]

    for e in range(E):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        arr[r][c] = 1
        

    # print(arr)

    value_r, value_c = map(int, input().split())
    find_r = value_r - 1
    find_c = value_c - 1

    print("#{} {}".format(tc+1, my_func(arr, find_r)))