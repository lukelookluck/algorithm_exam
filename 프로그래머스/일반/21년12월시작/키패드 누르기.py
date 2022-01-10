def solution(numbers, hand):
    answer = ''
    num = {'1': [0, 0], '2': [1, 0], '3': [2, 0], 
           '4': [0, 1], '5': [1, 1], '6': [2, 1], 
           '7': [0, 2], '8': [1, 2], '9': [2, 2], 
           '*': [0, 3], '0': [1, 3], '#': [2, 3], }
    
    L, R = [0, 3], [2, 3]
    
    for n in numbers: 
        if n in [1, 4, 7]:
            answer += 'L'
            L = num[str(n)]
        elif n in [3, 6 ,9]:
            answer += 'R'
            R = num[str(n)]
        else:
            L_len = abs(L[0] - num[str(n)][0]) + abs(L[1] - num[str(n)][1])
            R_len = abs(R[0] - num[str(n)][0]) + abs(R[1] - num[str(n)][1])
            if L_len > R_len:
                answer += 'R'
                R = num[str(n)]
            elif L_len < R_len:
                answer += 'L'
                L = num[str(n)]
            else:
                if hand == 'right':
                    answer += 'R'
                    R = num[str(n)]
                else:
                    answer += 'L'
                    L = num[str(n)]
                
    return answer
