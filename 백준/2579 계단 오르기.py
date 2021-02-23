import sys

N = int(sys.stdin.readline().strip())
myarr = []
check = [0] * N

for _ in range(N):
    myarr.append(int(sys.stdin.readline().strip()))
if N <= 2:
    print(sum(myarr[:N]))
else:
    check[0], check[1] = myarr[0], myarr[0] + myarr[1]

    for i in range(2, N):
        check[i] = max(myarr[i] + myarr[i-1], myarr[i] + check[i-2])
        myarr[i] += check[i-2]

    print(max(myarr[N-1], check[N-1]))
