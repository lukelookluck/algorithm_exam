from collections import deque
import sys

def solution(x, mode):
    check = [-1] * (n+1)
    check[x] = 0
    my_dq = deque()
    my_dq.append(x)

    while my_dq:
        x = my_dq.popleft()
        for num, weight in arr[x]:
            if check[num] == -1:
                check[num] = check[x] + weight
                my_dq.append(num)

    if mode == 0:
        return check.index(max(check))

    else:
        return max(check)


n = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

print(solution(solution(1, 0), 1))


