import sys

N = sys.stdin.readline().strip()
check = [0] * 10

for n in N:
    check[int(n)] += 1

for i in range(9, -1, -1):
    if check[i]:
        print(str(i) * check[i], end='')