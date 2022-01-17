from collections import defaultdict
import operator


def solution(s):
    answer = []
    temp = defaultdict()

    t = ''
    for j in s:
        if j.isdigit():
            t += j
        else:
            if t.isdigit():
                if t in temp:
                    temp[t] += 1
                else:
                    temp[t] = 1
            t = ''
    temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
    # print(temp)
    for k in temp:
        answer.append(int(k[0]))

    return answer