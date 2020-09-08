import sys, time
sys.stdin = open('하나로.txt')

st = time.time()


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    key = [float('inf') for _ in range(N)]
    key[0] = 0
    visited = [False] * N

    for _ in range(1, N):
        # 최소 key 찾기
        min_key = float('inf')
        start = -1
        for i in range(N):
            if key[i] < min_key and not visited[i]:
                min_key = key[i]
                start = i
            # key 갱신
        visited[start] = True
        for i in range(1, N):
            if not visited[i]:
                dist = (x_list[start] - x_list[i]) ** 2 + (y_list[start] - y_list[i]) ** 2
                if dist < key[i]:
                    key[i] = dist
    cost = sum(key) * tax
    print('#{} {}'.format(test_case, round(cost)))
print(time.time() - st)