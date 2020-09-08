import sys
sys.stdin = open('문자열 비교.txt')

T = int(input())

for tc in range(T):
    str1 = str(input())
    str2 = str(input())
    k = 0
    result = 0
    count = 0
    # for i in range(len(str1)-1, -1, -1):
    for j in range(0, len(str2)):
        if str1[-1] == str2[j]:
            k = j + 1
            for l in range(0, len(str1) - 1):
                if str1[l] != str2[k - len(str1) + l]:
                    result = 0
                    break
                else:
                    result = 1

            if result == 1:
                count += 1

    print("#{} {}".format(tc + 1, count))