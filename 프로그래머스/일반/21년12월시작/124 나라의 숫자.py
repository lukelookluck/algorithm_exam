def solution(n):
    answer = ''
    
    while n:
        nn = n % 3
        if nn == 1:
            answer = '1' + answer
        elif nn == 2:
            answer = '2' + answer 
        elif nn == 0:
            answer = '4' + answer
        
        n //= 3
        
        if not nn:
            n -= 1
    
    return answer
