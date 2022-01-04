def solution(brown, yellow):
    answer = []
    my_sum = brown + yellow
    for i in range(3, (my_sum // 3) + 1):
        my_x = my_sum // i
        if my_sum % i == 0 and yellow == (i - 2) * (my_x - 2):
            return [my_x, i]

    return answer

b = 24
y = 24
print(solution(b, y))