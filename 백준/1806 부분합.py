import sys

N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split())) + [0]
start, end = 0, 1
answer = float('inf')
temp = data[start]

while start < end < N+1:
    if temp >= S:
        if answer > end - start:
            answer = end - start
        temp -= data[start]
        start += 1
    else:
        temp += data[end]
        end += 1

print(answer if answer != float('inf') else 0)