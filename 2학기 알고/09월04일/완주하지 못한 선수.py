def solution(participant, completion):
    answer = ''
    my_list = {}
    for i in participant:
        if i in my_list:
            my_list[i] += 1
        else:
            my_list[i] = 1

    for i in completion:
        if i in my_list:
            my_list[i] -= 1

    for key, value in my_list.items():
        if value != 0:
            answer = key
            break

    return answer