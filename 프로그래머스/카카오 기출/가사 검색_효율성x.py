import sys
sys.stdin = open('가사 검색.txt')

def check(query):
    if query in used:
        return used[query]

    q_bool = False
    if query[0] == '?':
        query = query[::-1]
        q_bool = True

    n = 0
    len_query = len(query)
    for word in words:
        if q_bool:
            word = word[::-1]
        if query == '?'*len(word):
            n += 1
            continue
        if len(word) == len_query:
            my_bool = True
            for i in range(len_query):
                # print(word[i], query[i])
                if word[i] != query[i]:
                    if query[i] == '?':
                        break
                    else:
                        my_bool = False
                        break
            # print(my_bool)
            if my_bool:
                n += 1
            # print('======')
    if query not in used:
        used[query] = n
    return n


T = int(input())
for tc in range(T):
    words = list(map(str, input().split()))
    queries = list(map(str, input().split()))
    used = {}
    answer = []

    for query in queries:
        answer.append(check(query))
        # print('-------')
        print(used)
    print(answer)