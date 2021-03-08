import sys


def solution(mid):
    temp = mid // N
    cnt = temp * N

    for i in range(temp + 1, N+1):
        cnt += mid // i

        if cnt >= k:
            break

    return cnt


N = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

start, end = 1, N*N

while start <= end:
    middle = (start + end) // 2

    if solution(middle) >= k:
        end = middle - 1
    else:
        start = middle + 1

print(start)
