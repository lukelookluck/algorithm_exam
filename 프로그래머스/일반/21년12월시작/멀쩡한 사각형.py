import math

def solution(w,h):
    a, b = max(w, h), min(w, h)
    
    while (b != 0):
        temp = a % b
        a = b
        b = temp

    return w * h - (w + h - a)
