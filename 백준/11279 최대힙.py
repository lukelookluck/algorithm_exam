import heapq, sys

N = int(sys.stdin.readline().strip())
heap = []

for n in range(N):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        # 힙에서 튜플 원소는 튜플 중 인덱스 0 값을 기준으로 정렬됨
        # 따라서 최대 힙을 구현하기 위에, (-x, x)로 된 튜플 원소 추가
        heapq.heappush(heap, (-x, x))
