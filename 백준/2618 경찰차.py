N=int(input())
W=int(input())
wl=[[1,1],[N,N]]
for i in range(W):
    wl.append(list(map(int,input().split())))

def dis(x,y):
    return abs(wl[x][0]-wl[y][0])+abs(wl[x][1] - wl[y][1])

dp=[[0]*(W+2) for i in range(W+2)]
car=[[-1]*(W+2) for i in range(W+2)]
car[1][0]=1 # 0 1

print(dp, car)

for i in range(2,W+2):
    mv = 2 * N * W
    for j in range(i-1):
        dp[i][j]=dp[i-1][j]+dis(i,i-1)
        print(wl)
        print(i, j)
        print(*dp, sep='\n')
        car[i][j]=car[i-1][j]
        if mv>dp[i-1][j]+dis(i,j):
            mv=dp[i-1][j]+dis(i,j)
            car[i][i-1]=(car[i-1][j]+1)%2
        print('-------------')
    print('mv', mv)
    dp[i][i-1]=mv
    print(*dp, sep='\n')

    print('===============')


mv = 2 * N * W
for i in range(W+1):
    if mv>dp[W+1][i]:
        mv=dp[W+1][i]
        r=i
c=W+1

print(mv)

li=[(c,r)]
while 2<c:

    if r==c-1:
        for j in range(c-1):
            if dp[c - 1][j] + dis(c, j) == dp[c][r]:
                r=j
                break
    c-=1
    li.append((c, r))

for i in range(W-1,-1,-1):
    print((car[li[i][0]][li[i][1]]+1))