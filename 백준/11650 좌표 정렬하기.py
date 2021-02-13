import sys

N = int(sys.stdin.readline())
# check = [[] for _ in range(200001)]
#
# for n in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     check[x + 100000].append(y)
#
# for i in range(200001):
#     if len(check[i]) > 0:
#         for j in sorted(check[i]):
#             print(i - 100000, j)

check = []
for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    check.append((x, y))

for i in sorted(check):
    print(i[0], i[1])