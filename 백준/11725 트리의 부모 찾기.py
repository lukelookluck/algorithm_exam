import sys
from collections import deque




N = int(sys.stdin.readline())
data = [[] for _ in range(N+1)]
check = [0] * (N+1)
ans = [0] * (N+1)

for n in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

my_q = deque()
my_q.append(1)

while my_q:
    x = my_q.popleft()
    check[x] = 1

    for dt in data[x]:
        if not check[dt]:
            ans[dt] = x
            my_q.append(dt)

print(*ans[2:], sep='\n')