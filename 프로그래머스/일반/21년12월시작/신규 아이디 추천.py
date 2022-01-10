from string import ascii_lowercase

def solution(new_id):
    new_id = new_id.lower()
    
    alphabet = list(ascii_lowercase) + [str(i) for i in range(0, 10)] + ['-', '_', '.']
    new_id = ''.join(x for x in new_id if x in alphabet)
    # print(new_id)
    my_bool = False
    temp = ''
    for ni in new_id:
        if ni == '.':
            if not my_bool:
                temp += ni
                my_bool = True
            else:
                continue
        else:
            temp += ni
            my_bool = False
    new_id = temp
    # print(new_id)
    if new_id[0] == '.':
        if len(new_id) > 1:
            new_id = new_id[1:]
        else:
            new_id = ''
    elif new_id[-1] == '.':
        if len(new_id) > 1:
            new_id = new_id[:-1]
        else:
            new_id = ''
    # print(new_id)
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # print(new_id)
    
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    # print(new_id)
    
    return new_id
