import sys, time
sys.stdin = open('상원이 생파.txt')


def my_func(x, depth):
    global cnt
    # print("depth", depth, cnt)
    if depth == 2:
        return
    if friend_relation[x]:
        for i in friend_relation[x]:
            # print(i)
            if check_list[i] == -1:
                check_list[i] = 1
                cnt += 1
            # print(check_list)
            my_func(i, depth+1)
    else:
        return


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    friend_relation = [[] for _ in range(N)]
    check_list = [-1 for _ in range(N)]
    for m in range(M):
        temp_var1, temp_var2 = map(int, input().split())
        friend_relation[temp_var1-1].append(temp_var2-1)
        friend_relation[temp_var2-1].append(temp_var1-1)
    cnt = 0
    print(friend_relation)
    check_list[0] = 1
    my_func(0, 0)
    print(check_list)
    print("#{} {}".format(tc+1, cnt))


