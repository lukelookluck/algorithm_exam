from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
data = deque(map(int, sys.stdin.readline().split()))
my_d = deque(range(1, N+1))
idx = 0
ans = 0

for _ in range(M):
    find_idx = my_d.index(data[0])
    ans += min(abs(find_idx - idx), abs(len(my_d) - abs(find_idx - idx)))
    my_d.remove(data[0])
    data.popleft()
    idx = find_idx

print(ans)
