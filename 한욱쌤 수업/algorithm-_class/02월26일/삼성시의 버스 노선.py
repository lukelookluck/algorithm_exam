import sys
sys.stdin = open('삼성시의 버스 노선.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    AB_list = []
    my_min = float('inf')
    my_max = 0
    P_arr = list(0 for _ in range(5001))
    for n in range(N):
        temp = list(map(int, input().split()))
        for j in range(temp[0], temp[1] + 1):
            P_arr[j] += 1

    # print(AB_list)
    P = int(input())
    # print(my_min, my_max)
    # print(P)

    # print(P_arr)
    # for i in range(0, len(AB_list), 2):
    #     for j in range(AB_list[i], AB_list[i+1]+1):
    #         P_arr[j] += 1
    # print(P_arr)
    print("#{}".format(tc+1), end= ' ')
    t = []
    for p in range(P):
        C = int(input())
        t.append(P_arr[C])
    print(*t)





    # print("#{}".format(tc+1), *P_arr)
