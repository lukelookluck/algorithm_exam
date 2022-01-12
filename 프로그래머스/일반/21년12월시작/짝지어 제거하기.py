from string import ascii_lowercase

def solution(s):
    answer = -1
    my_list = [s[0]]
    
    for x in s[1:]:
        if not my_list:
            my_list.append(x)
            continue
        if my_list[-1] == x:
            my_list.pop()
        else:
            my_list.append(x)
        
    answer = 0 if len(my_list) != 0 else 1
        
    return answer
