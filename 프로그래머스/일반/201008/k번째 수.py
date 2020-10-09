def solution(array, commands):
    answer = []

    for command in commands:                            # commands 에서 command 하나 꺼내기
        temp_array = array[command[0]-1:command[1]]     # command 값으로 array 자르기
        sorted_array = sorted(temp_array)               # 자른 array 정렬
        answer.append(sorted_array[command[2]-1])       # 정렬한 array 중 command 값 번째 result에 추가

    return answer



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print('answer', solution(array, commands))