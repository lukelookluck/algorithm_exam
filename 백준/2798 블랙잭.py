import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            my_sum = cards[i] + cards[j] + cards[k]
            if ans < my_sum <= M:
                ans = my_sum
print(ans)


