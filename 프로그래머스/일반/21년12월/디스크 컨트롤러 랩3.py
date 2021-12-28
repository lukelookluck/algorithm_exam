import heapq


def solution(jobs):
    answer, s, n, i = 0, -1, 0, 0
    heap = []

    while i < len(jobs):
        for j in jobs:
            if s < j[0] <= n:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap):
            h = heapq.heappop(heap)
            s = n
            n += h[0]
            answer += n - h[1]
            i += 1
        else:
            n += 1

    return int(answer / len(jobs)
