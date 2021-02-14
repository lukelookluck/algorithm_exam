from collections import deque
import sys

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = deque(map(int, sys.stdin.readline().split()))
    cnt = 1

    while True:
        if len(arr) == 1:
            print(cnt)
            break

        x = arr.popleft()

        if x >= max(arr):
            if M == 0:
                print(cnt)
                break
            else:
                M -= 1
            cnt += 1

        else:
            if M == 0:
                M = len(arr)
            else:
                M -= 1
            arr.append(x)
