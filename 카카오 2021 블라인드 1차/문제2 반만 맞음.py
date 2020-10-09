from itertools import combinations

def solution(orders, course):
    answer = []
    menu_set = {}
    for i in range(len(orders)):
        for menu in orders[i]:
            if menu not in menu_set:
                menu_set[menu] = [i]
            else:
                menu_set[menu] += [i]
    menu_set1 = {}
    for key, value in menu_set.items():
        if len(value) >= 2:
            menu_set1[key] = value
    print(menu_set1)
    for i in course:
        answer += check(menu_set1, i)
    print(answer)
    len_answer = len(answer)
    last_answer = []
    max_list = [2] * (max(course) + 1)
    for i in range(0, len_answer-1):
        my_bool = True
        for j in range(i+1, len_answer):
            if answer[i][1] == answer[j][1]:
                my_bool = False
        if my_bool is True:
            last_answer.append((answer[i][0], len(answer[i][1])))
            if max_list[len(answer[i][0])] < len(answer[i][1]):
                max_list[len(answer[i][0])] = len(answer[i][1])
    last_answer.append((answer[-1][0], len(answer[-1][1])))
    print(max_list)
    print(last_answer)
    last_last = []
    for i in last_answer:
        if i[1] == max_list[len(i[0])]:
            last_last.append(''.join(sorted(i[0])))
    print(last_last)
    print(sorted(last_last))


def check(menu_set1, N):
    result = []
    com_list = []
    c = combinations(menu_set1, N)
    com_list.extend(c)
    print(com_list)
    for i in com_list:
        print(i)
        temp = set(menu_set1[i[0]])
        for j in range(1, len(i)):
            print(menu_set1[i[j]])
            print(temp)
            temp = find_intersection(temp, menu_set1[i[j]])
            if len(temp) < 2:
                print('ads')
                break
        if len(temp) >= 2:
            result.append((''.join(i), temp))
    return result
        # print(temp)


def find_intersection(temp, next):
    return temp & set(next)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH", 'ACFG']
course = [2,3,4]
solution(orders, course)