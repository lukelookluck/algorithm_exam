import sys

N = int(sys.stdin.readline())
# data = [[] for _ in range(201)]
data = {str(i): [] for i in range(201)}

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    data[age] += [name]

for k, v in data.items():
    for d in v:
        print(k, d)