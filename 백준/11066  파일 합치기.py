import sys

T = int(sys.stdin.readline().strip())
for tc in range(T):
    K = int(sys.stdin.readline().strip())
    myList = [0] + list(map(int, sys.stdin.readline().split()))
    myArr = [[0]*(K+1) for _ in range(K+1)]

    for i in range(1, K+1):
        myArr[0][i] = myList[i] + myArr[0][i-1]

    for i in range(2, K+1): # 2 3 4
        for j in range(1, K+2-i): # 123 12 1
            myArr[j][i+j-1] = min([myArr[j][j+k] + myArr[j+k+1][j+i-1] for k in range(i-1)]) + myArr[0][i+j-1] - myArr[0][j-1]

    print(myArr[1][K])
