import sys
sys.stdin = open('백만 장자 프로젝트.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    my_max = float('-inf')
    my_result = 0
    for i in range(N-1, -1, -1):
        if data[i] > my_max:
            my_max = data[i]
            # my_result = 0
        my_result += my_max - data[i]

    print("#{} {}".format(tc+1, my_result))