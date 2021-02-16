import sys

N, C = map(int, sys.stdin.readline().split())
houses = []

for n in range(N):
    houses.append(int(sys.stdin.readline().strip()))

houses.sort()
start, end = 1, houses[-1] - houses[0]
ans = 0

while start <= end:
    gap = (start + end) // 2
    x = houses[0]
    cnt = 1
    for i in range(1, N):
        if houses[i] >= x + gap:
            cnt += 1
            x = houses[i]
    if cnt >= C:
        start = gap + 1
        ans = gap
    else:
        end = gap - 1
print(ans)