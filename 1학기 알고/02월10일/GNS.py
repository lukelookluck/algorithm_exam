import sys
sys.stdin = open('GNS.txt')

T = int(input())
for tc in range(T):
    N, M = map(str, input().split())
    data = list(map(str, input().split()))


    digit_count = []
    digit_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in digit_list:
        digit_count.append(data.count(i))

    print("#{}".format(tc+1))
    for i in range(10):
        print((digit_list[i] + ' ') * digit_count[i], end=' ')
