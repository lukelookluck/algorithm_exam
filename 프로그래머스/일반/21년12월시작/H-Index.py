def solution(citations):
    citations = sorted(citations, reverse=True)
    print(citations)
    answer = list(map(min, enumerate(citations, start=1)))
    print(list(enumerate(citations, start=1)))
    print(answer)
    return max(answer)



a = [3, 0, 6, 1, 5]
solution(a)