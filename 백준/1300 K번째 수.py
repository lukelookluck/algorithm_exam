import sys

N = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

start, end = 1, N*N

while start <= end:
    middle = (start + end) // 2
    cnt = 0

    for i in range(1, N+1):
        cnt += min(N, middle // i)

        if cnt >= k:
            break

    if cnt >= k:
        end = middle - 1
    else:
        start = middle + 1

print(start)
