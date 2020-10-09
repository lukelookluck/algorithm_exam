def solution(info, query):
    answer = []
    info_list = []
    query_list = []
    for i in info:
        info_list.append(list(map(str, i.split())))
    print(info_list)
    for i in query:
        query_list.append(list(map(str, i.split())))
    print(query_list)

    for i in query_list:
        temp = []
        cnt = 0
        for j in range(0, len(i), 2):
            temp.append(i[j])
        temp.append(i[-1])
        print(temp)
        for k in info_list:
            n = 0
            my_bool = True
            while n != 5:
                if n < 4:
                    if temp[n] == '-':
                        n += 1
                        continue
                    if temp[n] != '-' and k[n] != temp[n]:
                        my_bool = False
                        break
                else:
                    if int(k[n]) < int(temp[n]):
                        my_bool = False
                        break
                n += 1
            if my_bool is False:
                continue

            if my_bool is True:
                print('akasdasl')
                print(k)
                cnt += 1

        answer.append(cnt)
    print(answer)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)
