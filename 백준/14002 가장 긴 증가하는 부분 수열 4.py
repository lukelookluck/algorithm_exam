import sys

A = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
check = [1] * A

for i in range(A-1, -1, -1):
    for j in range(i-1, -1, -1):
        if data[i] > data[j] and check[i] >= check[j]:
            check[j] += 1

key = max(check)
print(key)
for i in range(A):
    if check[i] == key:
        print(data[i], end=' ')
        key -= 1