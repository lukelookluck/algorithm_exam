import sys
sys.stdin = open('레벨2-2.txt')

N = int(input())
for i in range(N):
    n = int(input())
    my_list = list(range(n+1))
    print(my_list)

    my_sum = [0]
    cnt = 1
    result = 0
    while my_sum[-1] != n:

        print(my_sum)
        if sum(my_sum) < n:
            if cnt < n + 1:
                my_sum.append(my_list[cnt])
                cnt += 1

        elif sum(my_sum) == n:
            # print('n이랑 같아', my_sum)
            result += 1
            if cnt < n + 1:
                my_sum.append(my_list[cnt])
                cnt += 1

        else:
            my_sum.pop(0)
            # print('pop!', my_sum)

    print(result+1)