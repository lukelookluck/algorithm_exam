from heapq import heappop, heappush
import sys


N = int(sys.stdin.readline().strip())
W = int(sys.stdin.readline().strip())
# check = [float('inf')] * (W+1)
check = [[float('inf')] * (W+1) for _ in range(W+1)]
answer = 0
route = []
f1, f2 = 1, 1
s1, s2 = N, N

dist = [0]
for k in range(W):
    dist.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(1, W+1):
    for j in range(1, W+1):
        x = max(i, j)

        temp1 = abs(f1 - dist[i][0]) + abs(f2 - dist[i][1])
        temp2 = abs(s1 - dist[i][0]) + abs(s2 - dist[i][1])

        check[0][i] = temp2
        check[i][0] = temp1

        if temp1 > temp2:
            answer += temp2
            route.append(2)
            s1, s2 = dist[i][0], dist[i][1]
        else:
            answer += temp1
            route.append(1)
            f1, f2 = dist[i][0], dist[i][1]
        print(*check, sep='\n')

print(answer)
print(*route, sep='\n')