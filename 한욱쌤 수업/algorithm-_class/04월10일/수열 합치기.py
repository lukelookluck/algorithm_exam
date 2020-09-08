import sys
sys.stdin = open('수열 합치기.txt')

T = int(input())
for tc in range(T):
    N, M = map(int ,input().split())

    result_list = [*map(int, input().split())]
    for m in range(M - 1):
        temporary_list = [*map(int, input().split())]
        # print(temporary_list)
        my_bool = False
        L = M

        for i in range(L):
            # print(i)
            if result_list[i] > temporary_list[0]:
                for t in temporary_list[::-1]:
                    result_list.insert(i, t)
                my_bool = True
                # print(result_list)
                L += L
                break
        if my_bool is False:
            for t in temporary_list[::]:
                result_list.append(t)
            # print(result_list)
    print("#{}".format(tc+1), *result_list[-1:-11:-1])