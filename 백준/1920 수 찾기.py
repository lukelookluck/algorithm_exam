from bisect import bisect
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_data = list(map(int, sys.stdin.readline().split()))

A.sort()
print(A)
for m in M_data:
    i = bisect(A, m) - 1
    # print(i)
    # print(A[i])
    if i != len(A) and A[i] == m:
        print(1)
    else:
        print(0)