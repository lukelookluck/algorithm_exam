import sys


def solution():
    for i in range(1, n+1):
        if i == 1:
            check[1] = data[1]
        elif i == 2:
            check[2] = data[1] + data[2]
        else:
            check[i] = max(
                data[i] + data[i-1] + check[i-3],
                data[i] + check[i-2],
                check[i-1]
            )



n = int(sys.stdin.readline().strip())
data = [0]
check = [0] * (n+1)

for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

solution()
print(check[n])