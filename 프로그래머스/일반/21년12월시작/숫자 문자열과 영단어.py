def solution(s):
    answer = 0
    trans = {"zero" : 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for k, v in trans.items():
        if k in s:
            print(k, v)
            s = s.replace(k, str(v))
    
    return int(s)


