import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
answer = float('-inf')
temp = 0

for dt in data:
    temp += dt
    # print(temp)
    if answer < temp:
        answer = temp

    if temp <= 0:
        temp = 0

    # print('answer', answer)

print(answer)