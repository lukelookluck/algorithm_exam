import sys

n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
key = int(sys.stdin.readline().strip())
answer = 0
s, e = 0, n-1

while s < e:
    my_sum = arr[s] + arr[e]
    if my_sum == key:
        answer += 1
        e -= 1
    elif my_sum < key:
        s += 1
    else:
        e -= 1

print(answer)