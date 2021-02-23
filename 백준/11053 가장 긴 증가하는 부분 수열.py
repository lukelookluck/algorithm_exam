import sys

N = int(sys.stdin.readline().strip())
myarr = list(map(int, sys.stdin.readline().split()))
check = [1] * N

for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if myarr[i] > myarr[j] and check[i] >= check[j]:
            check[j] += 1

print(max(check))

