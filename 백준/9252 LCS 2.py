import sys

'''
def solution():
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                check[i+1][j+1] = check[i][j] + str1[i]
            else:
                if len(check[i][j+1]) >= len(check[i+1][j]):
                    check[i+1][j+1] = check[i][j+1]
                else:
                    check[i+1][j+1] = check[i+1][j]
    return len(check[-1][-1])


str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
check = [[''] * (len(str2) + 1) for _ in range(len(str1) + 1)]

print(solution())
print(check[-1][-1])
'''
def solution():
    answer = ''
    for i in range(len(str1)):
        temp = ''
        for j in range(len(str2)):
            if len(temp) < len(check[j]):
                temp = check[j]
            elif str1[i] == str2[j]:
                check[j] = temp + str1[i]

    for ck in check:
        if len(answer) < len(ck):
            answer = ck

    if len(answer):
        print(len(answer), answer, sep='\n')
    else:
        print(0)


str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
check = [''] * len(str2)
solution()
