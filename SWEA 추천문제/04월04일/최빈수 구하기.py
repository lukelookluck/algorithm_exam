import sys
sys.stdin = open('최빈수 구하기.txt')

T = int(input())
for tc in range(T):
    cn = int(input())
    data = [*map(int, input().split())]
    count_dic = {}
    for i in data:
        if i not in count_dic.keys():
            count_dic[i] = 1
        else:
            count_dic[i] += 1
    result = 0
    for digit, cnt in count_dic.items():
        if cnt == max(count_dic.values()):
            if result < digit:
                result = digit
    print("#{} {}".format(tc+1, result))