def solution(n):
    a, b, cnt = 0, 1, 0
    
    while cnt != n:
        a, b = b, a + b
        cnt += 1
        
    return a % 1234567
