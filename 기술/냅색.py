import sys
sys.stdin = open('냅색.txt')

N, H, M = map(int, sys.stdin.readline().split())
myarr = [[[0, 0] for _ in range(H+1)] for _ in range(M+1)]
res = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    res.append((a, b))

for i in range(1, M+1):
    for j in range(H+1):
        which = res[i-1][0]
        mytime = res[i-1][1]

        if j >= mytime:
            myarr[i][j][which-1] = max(myarr[i-1][j - mytime][which-1] + mytime, myarr[i-1][j][which-1])
            myarr[i][j][2-which] = myarr[i - 1][j][2-which]

        else:
            myarr[i][j] = myarr[i - 1][j]

print(*myarr, sep='\n')
