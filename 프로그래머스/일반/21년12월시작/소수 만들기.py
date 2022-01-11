from itertools import combinations 
import math

def solution(nums):
    answer = 0
    check = [0] * len(nums)
    
    my_list = list(combinations(nums, 3))
    
    for ml in my_list:
        my_sum = sum(ml)
        my_bool = False
        for a in range(2, int(math.sqrt(my_sum)) + 1):
            if my_sum % a == 0:
                my_bool = True
                break
        if not my_bool:
            answer += 1

    
    return answer
