import sys

K, N = map(int, sys.stdin.readline().split())
lines = []
for k in range(K):
    data = int(sys.stdin.readline().strip())
    lines.append(data)

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid

        if cnt >= N:
            break
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)