def solution(new_id):
    answer = ''
    temp = ''
    print(new_id)
    temp = new_id.lower()
    print(temp)
    for i in temp:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i
    print(answer)
    temp = ''
    my_bool = True
    for i in answer:
        if i == '.':
            if my_bool is True:
                my_bool = False
                temp += i
        else:
            my_bool = True
            temp += i
    print(temp)
    answer = ''
    if temp[0] == '.':
        temp = temp[1:]
    if temp != '':
        if temp[-1] == '.':
            temp = temp[:-1]
    print(temp)
    if temp == '':
        temp += 'a'
    if len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == '.':
            temp = temp[:-1]
    print(temp)
    if len(temp) <= 2:
        last_word = temp[-1]
        while len(temp) < 3:
            temp += last_word
    print(temp)
    answer = temp
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)