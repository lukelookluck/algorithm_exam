import heapq


def solution(scoville, K):
    answer = 0
    my_q = []

    for s in scoville:
        heapq.heappush(my_q, s)

    while my_q[0] < K:
        try:
            heapq.heappush(my_q, heapq.heappop(my_q) + heapq.heappop(my_q) * 2)
            answer += 1
        except IndexError:
            return -1

    return answer


s = [1, 2, 3, 9, 10, 12]
k = 150
print(solution(s, k))