import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

check = [0]
temp = [data[0]]

for i in range(1, N):
    x = data[i]

    if temp[-1] < x:
        temp.append(x)
        check.append(len(temp) - 1)
    else:
        idx = bisect_left(temp, x)
        temp[idx] = x
        check.append(idx)

print(len(temp))

cnt = max(check)
answer = ''

for i in range(N-1, -1, -1):
    if check[i] == cnt:
        answer = str(data[i]) + ' ' + answer
        cnt -= 1
print(answer)