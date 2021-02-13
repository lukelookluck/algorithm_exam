import sys
from collections import deque
sys.stdin = open('1005 ACM Craft.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    building = [[] for _ in range(N+1)]
    time = [0 for _ in range(N+1)]
    sequence = [0 for _ in range(N+1)]

    for kc in range(K):
        f, s = map(int, sys.stdin.readline().split())
        building[f].append(s)
        sequence[s] += 1

    key = int(input())
    my_q = deque()

    for i in range(1, N+1):
        if sequence[i] == 0:
            my_q.append(i)
            time[i] = D[i]

    while my_q:
        x = my_q.popleft()
        for i in building[x]:
            sequence[i] -= 1
            time[i] = max(time[x] + D[i], time[i])
            if sequence[i] == 0:
                my_q.append(i)

    print(time[key])