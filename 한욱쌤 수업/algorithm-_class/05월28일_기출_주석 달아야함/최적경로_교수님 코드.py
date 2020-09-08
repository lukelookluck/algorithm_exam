import time
start_time = time.time()

import sys
sys.stdin = open("최적 경로.txt")
T = int(input())
def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def perm(n, k, cur_dist):
    global ans
    if cur_dist > ans: return

    if k == n:
        cur_dist += D[t[k]][t[N+1]]
        if cur_dist < ans : ans = cur_dist
    else:
        for i in range(n):
            if visited[i+1]: continue
            # t[k+1] = A[i+1]
            t[k+1] = i+1
            visited[i+1] = 1
            perm(n, k+1, cur_dist + D[t[k]][t[k+1]])
            visited[i+1] = 0

for tc in range(T):
    N = int(input())                        # 고객수
    temp = list(map(int, input().split()))
    A = list(range(N+2))
    t = [0] + [0] * N + [N+1]                # 회사-고객-집
    visited = [0] * (N+2)                    # 방문처리
    P = [(0,0) for _ in range(N+2)]          # 좌표
    D = [[0 for _ in range(N+2)] for _ in range(N+2)]  # 거리
    ans = 0x7fffffff

    P[0] = (temp[0], temp[1])   # 회사
    P[N+1] = (temp[2], temp[3]) # 집

    idx = 1
    for i in range(4, len(temp), 2): # 고객
        P[idx] = (temp[i], temp[i+1])
        idx += 1

    for i in range(N+1):   # 메모이제이션
        for j in range(i+1, N+2, 1):
            D[j][i] = D[i][j] = getD(P[i], P[j])

    perm(N, 0, 0)
    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')