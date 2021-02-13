import sys

N = int(sys.stdin.readline())
data = set()

for _ in range(N):
    data.add(sys.stdin.readline().strip())

print(*sorted(list(data), key=lambda x: (len(x), x)), sep='\n')
