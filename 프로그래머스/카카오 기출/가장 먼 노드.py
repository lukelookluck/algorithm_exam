from queue import PriorityQueue
from collections import defaultdict

def solution(n, edge):
    pq = PriorityQueue()

    dist = [999999 for x in range(n + 1)]
    dist[1] = 0 # 1번 노드부터 시작, 0으로 초기화

    neighbors = defaultdict(list)
    for e in edge:  # 노드번호: key, 이웃한 노드들 list: value
        neighbors[e[0]].append(e[1])
        neighbors[e[1]].append(e[0])

    for i in range(1, n+1):
        pq.put((dist[i], i)) # 각 노드의 1번 노드로부터 떨어진 거리와 각 노드번호 저장

    while pq.qsize() > 0:
        pq_get = pq.get() # pq에서 하나 꺼내기

        if pq_get[0] == 99999: # 해당 노드의 1번 노드로부터 떨어진 거리가 유효하면
            break

        u = pq_get[1]   # u에 해당 노드번호 저장

        for nei in neighbors[u]:
            alt = dist[u] + 1 # alt: 해당 노드의 1번 노드로부터 떨어진 거리 + 1
            if alt < dist[nei]: # 해당 노드의 이웃들을 돌며 alt가 기존 값보다 작을 경우, 갱신해줌
                dist[nei] = alt
                pq.put((alt, nei)) # 기존 값보다 작을 경우, 그 값을 토대도 주변 이웃을 다시 계산해야함

    answer = dist.count(max(dist[1:]))
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))