import sys
sys.stdin = open('파스칼의 삼각형.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    pas_list = []
    pas_list.append([1])
    pas_list.append([1, 1])
    if N >= 3: # 4
        for i in range(2, N): # 2, 3
            temp_list = []
            temp_list.append(1)
            for j in range(1, i): # i = 2, j = 1// i = 3, j = 1, 2
                temp_list.append(pas_list[i - 1][j - 1] + pas_list[i -1][j])
                # print(temp_list)
            temp_list.append(1)
            pas_list.append(temp_list)
    elif N == 1:
        pas_list = [[1]]
    print("#{}".format(tc+1))
    for i in pas_list:
        print(*i)
    print("---------------------")
