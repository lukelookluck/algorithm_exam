import sys
N, M = map(int, input().split())
data = [sys.stdin.readline().strip() for _ in range(N)]
ans = []

for a in range(N - 8 + 1):
    for b in range(M - 8 + 1):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2:
                    if data[a + i][b + j] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if data[a + i][b + j] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        ans.append(min(cnt1, cnt2))

print(min(ans))