import heapq


def solution(operations):
    answer = []
    q = []
    q_r = []

    for oper in operations:
        a, b = map(str, oper.split())
        b = int(b)

        if a == 'I':
            heapq.heappush(q, b)
            heapq.heappush(q_r, (-b, b))
        else:
            if len(q) == 0:
                continue
            elif b == 1:
                q.remove(heapq.heappop(q_r)[1])
            else:
                t = heapq.heappop(q)
                q_r.remove((-t, t))

    if q:
        return [heapq.heappop(q_r)[1], heapq.heappop(q)]
    else:
        return [0, 0]



a = ["I 7","I 5","I -5","D -1"]
print(solution(a))