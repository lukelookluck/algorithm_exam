import sys

N = int(sys.stdin.readline())
check = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    check.append((y, x))

for i in sorted(check):
    print(i[1], i[0])