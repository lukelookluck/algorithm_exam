from collections import deque


def solution(N, road, K):
    answer = 0
    inf = float('inf')
    my_arr = {i: [] for i in range(N + 1)}
    check = [inf for _ in range(N + 1)]
    my_q = deque([[1, 0]])
    check[1] = 0

    for r in road:
        a, b, c = r
        my_arr[a].append([b, c])
        my_arr[b].append([a, c])

    while my_q:
        x, y = list(my_q.popleft())
        for temp in my_arr[x]:
            a, b = temp
            if check[a] > check[x] + b:
                check[a] = check[x] + b
                my_q.append([a, check[x] + b])

    for x in check[1:]:
        if x <= K:
            answer += 1

    return answer
