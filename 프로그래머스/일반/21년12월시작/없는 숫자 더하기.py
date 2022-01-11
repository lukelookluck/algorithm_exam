def solution(numbers):
    answer = 0
    my_set = set(numbers)
    
    for i in range(1, 10):
        if i not in my_set:
           answer += i
    
    return answer
