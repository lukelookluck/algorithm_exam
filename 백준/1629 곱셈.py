import sys


A, B, C = map(int, sys.stdin.readline().split())
ans1 = A % C

if C % 2:
    print(ans1)
else:
    if ans1 == 1:
        print(ans1)
    else:
        print(1)

print(512 % 5)