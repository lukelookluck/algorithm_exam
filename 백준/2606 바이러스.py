import sys


def solution(idx):
    for i in arr[idx]:
        if check[i] == 0:
            check[i] = 1
            solution(i)


N = int(sys.stdin.readline().strip())
arr = {n: [] for n in range(1, N+1)}
D = int(sys.stdin.readline().strip())
check = [0] * (N + 1)

for _ in range(D):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

check[1] = 1
solution(1)
print(sum(check) - 1)