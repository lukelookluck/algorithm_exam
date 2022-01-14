from collections import defaultdict

def solution(tickets):
    answer = []
    my_dict = defaultdict(list)

    for t in tickets:
        my_dict[t[0]].append(t[1])
    # print(my_dict)

    for k in my_dict.keys():
        my_dict[k].sort(reverse=True)
    # print(my_dict)

    my_stack = ['ICN']
    while my_stack:
        temp = my_stack[-1]

        if my_dict[temp]:
            my_stack.append(my_dict[temp].pop())
        else:
            answer.append(my_stack.pop())

    answer.reverse()
    return answer

ti = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(ti)