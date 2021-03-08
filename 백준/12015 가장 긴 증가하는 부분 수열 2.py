from bisect import bisect_left
import sys


def solution(i):
    x = bisect_left(result, i)

    if len(result) <= x:
        result.append(i)
    else:
        result[x] = i


N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
result = []

for i in arr:
    solution(i)

print(len(result))
