import sys
sys.stdin = open('3665 최종 순위.txt')

T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    past_rank_num = [0] + list(map(int, sys.stdin.readline().split()))
    past_rank = [0] * (n+1)
    past_rank2 = [0] * (n+1)

    for i in range(n):
        past_rank[past_rank_num[i+1]] = i+1
        past_rank2[past_rank_num[i + 1]] = i + 1

    M = int(sys.stdin.readline())
    for m in range(M):
        a, b = map(int, sys.stdin.readline().split())
        rank_a, rank_b = past_rank[a], past_rank[b]
        if rank_a > rank_b:
            past_rank2[a] -= 1
            past_rank2[b] += 1
        else:
            past_rank2[a] += 1
            past_rank2[b] -= 1
        print(past_rank2)
    if len(list(set(past_rank2))) != n+1:
        print('IMPOSSIBLE')
    else:
        answer = [[] for _ in range(n)]
        for i in range(n):
            answer[past_rank2[i+1]-1] = i+1
        print(*answer)