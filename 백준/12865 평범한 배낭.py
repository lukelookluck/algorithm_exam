import sys


'''

def solution():
    for i in range(1, N+1):
        for j in range(1, K+1):
            weight = data[i-1][0]
            value = data[i-1][1]

            if weight <= j:
                answer[i][j] = max(answer[i-1][j-weight] + value, answer[i-1][j])
            else:
                answer[i][j] = answer[i-1][j]


N, K = map(int, sys.stdin.readline().split())
data = []
answer = [[0] * (K+1) for _ in range(N+1)]

for n in range(N):
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])

solution()
print(answer[N][K])
'''


def solution():
    for i in range(1, N+1):
        for j in range(K+1):
            weight = data[i-1][0]
            value = data[i-1][1]

            if j >= weight:
                check[i][j] = max(check[i-1][j-weight] + value, check[i-1][j])
            else:
                check[i][j] = check[i-1][j]


N, K = map(int, sys.stdin.readline().split())
data = []
check = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

solution()
print(*check, sep='\n')