import sys
sys.stdin = open('a.txt', 'r')

# def my_func(num):
#     str_num = str(num)
#     my_func = int(str_num[0]) + 1
#     return my_func

def find(data, k, n, m):
    data.insert(0,0)    #출발점 - 맨앞에 삽입
    data.append(n)       #종점 - 맨뒤에 추가
    last = 0            #마지막 충전기
    cnt = 0             #충전횟수
    for i in range(1, m + 2):
        if data[i] - data[i-1] > k :    #충전기 사이가 k보다 멀때
            return 0
        if data[i] > last + k:          #i충전기까지 갈 수 없으면
            last = data[i-1]
            cnt += 1
    return cnt




T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    # print(K)
    # print(N)
    # print(M)
    data = list(map(int, input().split()))
    # print(data)
    # distance = N / K
    # print(distance)
    # count = 0
    # verify = N
    # print(my_floor(distance))






    #
    # for i in range(M - 1, 0, -1):
    #     # print(data[i])
    #     if data[i] - data[i - 1] > K:
    #         count = 0
    #         break
    #         # print(result)
    # for j in range(M) :
    # if verify - data[j] <= K:
    #     verify = data[j]
    #     count += 1


            # count = (my_func(distance) - 1)
            # print((result))
    print("#{} {}".format(tc + 1, find(data, K, N, M)))