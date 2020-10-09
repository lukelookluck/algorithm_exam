def solution(citations):
    answer = 0

    citations = sorted(citations, reverse=True)
    c_list = []
    print(citations)
    for c in citations:
        cnt = 0
        for t in citations:
            if c <= t:
               cnt += 1
        c_list.append(min(cnt, c))
    print(c_list)
    c_list2 = []
    for c in c_list:
        cnt = 0
        for t in citations:
            if c <= t:
                cnt += 1
        c_list2.append(cnt)
    print(c_list2)

    for i in range(len(citations)):
        if c_list[i] <= c_list2[i]:
            if answer < c_list[i]:
                answer = c_list[i]
            # break
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))