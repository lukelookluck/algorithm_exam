import sys, heapq

N = int(sys.stdin.readline().strip())
my_heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        print(heapq.heappop(my_heap)[1] if my_heap else 0)
    else:
        # 힙에서 원소가 튜플일 경우, 튜플의 첫번째, 두번째, 세번째 값 순으로 정렬됨
        heapq.heappush(my_heap, (abs(x), x))