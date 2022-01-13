import math

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    len1, len2 = len(str1), len(str2)
    my_dict1, my_dict2 = {}, {}
    
    for i in range(0, len1):
        if i + 2 > len1 or not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        if str1[i:i+2] not in my_dict1:
            my_dict1[str1[i:i+2]] = 1  
        else:
            my_dict1[str1[i:i+2]] += 1
            
    for i in range(0, len2):
        if i + 2 > len2 or not str2[i].isalpha() or not str2[i+1].isalpha():
            continue
        if str2[i:i+2] not in my_dict2:
            my_dict2[str2[i:i+2]] = 1  
        else:
            my_dict2[str2[i:i+2]] += 1
    
    inner = 0
    
    for k, v in my_dict2.items():
        if k not in my_dict1:
            my_dict1[k] = v
        else:
            inner += min(my_dict1[k], v)
            my_dict1[k] = max(my_dict1[k], v)
        
    outer = sum(my_dict1.values())
    
    if outer:
        return math.trunc(inner / sum(my_dict1.values()) * 65536)
    else: 
        return 65536
