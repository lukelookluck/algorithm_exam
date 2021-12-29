def solution(array, commands):
    answer = []
    for c in commands:
        temp = sorted(array[c[0]-1:c[1]])
        print(temp)
        answer.append(temp[c[2]-1])

    return answer



a = [1, 5, 2, 6, 3, 7, 4]
b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a, b))