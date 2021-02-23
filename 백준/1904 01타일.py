import sys

N = int(sys.stdin.readline().strip())

a = 0
b = 1

for _ in range(N+1):
    a, b = b % 15746, (a + b) % 15746

print(a)