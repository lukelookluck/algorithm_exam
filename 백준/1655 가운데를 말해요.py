import sys, heapq

N = int(sys.stdin.readline().strip())
# 최대힙과 최소힙을 사용해서 해결
# 입력되어 만들어지는 정렬되는 배열을 반으로 나눠서
# 좌측을 최대힙에, 우측을 최소힙에 삽입해 나간다고 생각
max_q = []
min_q = []

for n in range(N):
    x = int(sys.stdin.readline().strip())

    # 삽입과정*
    if len(max_q) == len(min_q):
        heapq.heappush(max_q, (-x, x))
    else:
        heapq.heappush(min_q, (x, x))

    if min_q and max_q[0][1] > min_q[0][1]:
        # 삽입과정*에서 발생한 오류를 정정
        # 최대힙과 최소힙의 0번째 원소를 서로 바꿔주기
        factor_max = heapq.heappop(max_q)[1]
        factor_min = heapq.heappop(min_q)[1]
        heapq.heappush(max_q, (-factor_min, factor_min))
        heapq.heappush(min_q, (factor_max, factor_max))

    print(max_q[0][1])