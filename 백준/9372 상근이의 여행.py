import sys

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())

    print(N-1)
    for _ in range(M):
       sys.stdin.readline()