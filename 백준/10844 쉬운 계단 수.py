import sys

N = int(sys.stdin.readline().strip())
answer = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    answer[0][i] = 1

for i in range(1, N+1):
    for j in range(10):
        if j == 0:
            answer[i][j] = answer[i - 1][j + 1]
        elif j == 9:
            answer[i][j] = answer[i - 1][j - 1]
        else:
            answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j + 1]

print(sum(answer[N-1]) % 1000000000)
