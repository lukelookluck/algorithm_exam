import sys

T = int(sys.stdin.readline().strip())

myarr = [1, 1, 1, 2]

for _ in range(96):
    myarr.append(myarr[-3] + myarr[-2])

for tc in range(T):
    N = int(sys.stdin.readline().strip())
    print(myarr[N-1])