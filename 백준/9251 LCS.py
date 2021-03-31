import sys

'''
def solution():
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                check[i+1][j+1] = check[i][j] + 1
            else:
                check[i+1][j+1] = max(check[i][j+1], check[i+1][j])

    return check[len(str1)][len(str2)]


str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
check = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

print(solution())
'''


def solution():
    for i in range(len(str1)):
        temp = 0
        for j in range(len(str2)):
            if temp < check[j]:
                temp = check[j]
            elif str1[i] == str2[j]:
                check[j] = temp + 1
        print(check)
    return max(check)


str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
check = [0] * len(str2)

print(solution())
