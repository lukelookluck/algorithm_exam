import sys
sys.stdin = open('괄호검사.txt')

T = int(input())
for tc in range(T):
    data = str(input())
    key_list = []

    for i in data:
        if i == '{' or i == '(' or (i == '}' and '{' not in key_list) or (i == ')' and '(' not in key_list):
            key_list.append(i)
        if i =='}' and key_list[-1] == '{':
            key_list.pop()
        if i ==')' and key_list[-1] == '(':
            key_list.pop()

    if len(key_list) == 0:
        result = 1
    else:
        result = 0
    print("#{} {}".format(tc + 1, result))

