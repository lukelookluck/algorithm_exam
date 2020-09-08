import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(T):
    str1 = str(input())
    str2 = str(input())
    my_dict = {}

    for i in str1:
        my_dict[i]=str2.count(i)

    print("#{} {}".format(tc+1, max(my_dict.values())))


