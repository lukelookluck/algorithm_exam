import sys

N = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
s, e = 0, N-1
my_max = float('inf')
answer = []

while s < e:
    temp = arr[s] + arr[e]
    if my_max > abs(temp):
        my_max = abs(temp)
        answer = [arr[s], arr[e]]

    if abs(arr[s]) < abs(arr[e]):
        e -= 1
    else:
        s += 1

print(*answer)