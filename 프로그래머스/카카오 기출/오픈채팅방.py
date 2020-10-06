def solution(record):
    record = record
    answer = []
    temp = []
    name_set= {}
    for i in record:
        word = list(map(str, i.split()))
        if word[0] == 'Enter' or word[0] == 'Change':
            name_set[word[1]] = word[2]
            if word[0] == 'Enter':
                temp.append([word[1], 'Enter'])
        else:
            temp.append([word[1], 'Leave'])
    for log in temp:
        if log[1] == 'Enter':
            answer.append(name_set[log[0]] + '님이 들어왔습니다.')
        else:
            answer.append(name_set[log[0]] + '님이 나갔습니다.')
    # print(answer)
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)