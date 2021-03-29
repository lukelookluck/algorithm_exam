from bisect import bisect_left
import sys


N, C = map(int, sys.stdin.readline().split())
things = list(map(int, sys.stdin.readline().split()))

data1 = [0]
data2 = [0]

if N % 2:
    for i in range(N // 2):
        temp = []
        for x in data1:
            temp.append(things[i] + x)
        data1 += temp

    for i in range(N // 2, N):
        temp = []
        for x in data2:
            temp.append(things[i] + x)
        data2 += temp
else:
    for i in range(N // 2):
        temp = []
        for x in data1:
            temp.append(things[i] + x)
        data1 += temp

        temp = []
        for x in data2:
            temp.append(things[N // 2 + i] + x)
        data2 += temp

data2.sort()
answer = 0

for x in data1:
    if C - x >= 0:
        answer += bisect_left(data2, C - x + 1)

print(answer)