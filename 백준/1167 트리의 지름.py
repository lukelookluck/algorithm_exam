import sys
from collections import deque


def solution(index, mode):
    my_dq = deque()
    my_dq.append(index)
    check = [-1] * (V + 1)
    check[index] = 0

    while my_dq:
        x = my_dq.popleft()
        for index, weight in tree[x]:
            if check[index] == -1:
                check[index] = check[x] + weight
                my_dq.append(index)

    if mode == 0:
        return check.index(max(check))
    else:
        return max(check)


V = int(sys.stdin.readline())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, sys.stdin.readline().split()))
    a = data[0]
    for i in range((len(data) - 2) // 2):
        b, c = data[i*2 + 1], data[i*2 + 2]
        tree[a].append([b, c])
    
print(solution(solution(1, 0), 1))