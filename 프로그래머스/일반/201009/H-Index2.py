def solution(citations):
    citations = sorted(citations, reverse=True)
    for i in enumerate(citations, start=1):
        print(i)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

citations = [3, 0, 6, 1,1, 5]
print(solution(citations))