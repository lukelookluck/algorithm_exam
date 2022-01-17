def solution(n):
    cnt, i, j = 2, 1, 2
    
    while (n > cnt):
        j, i = j + i, j
        cnt += 1
    
    return j % 1000000007
