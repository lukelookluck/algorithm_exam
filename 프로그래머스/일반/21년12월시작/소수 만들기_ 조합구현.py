import math

def solution(nums):
    answer = 0
    check = [0] * len(nums)
    
    def comb(arr, idx):
        for i, a in enumerate(arr):
            if idx == 1:
                yield [a]
            else:
                for next in comb(arr[i+1:], idx-1):
                    yield [a] + next
                    
    for each in comb(nums, 3):
        my_sum = sum(each)
        my_bool = False
        for a in range(2, int(math.sqrt(my_sum)) + 1):
            if my_sum % a == 0:
                my_bool = True
                break
        if not my_bool:
            answer += 1

    
    return answer
