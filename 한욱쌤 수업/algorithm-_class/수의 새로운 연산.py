import sys
sys.stdin = open('수의 새로운 연산.txt')


def my_value(y, x):
    return x + (y+x-2)*(y+x-1)/2

T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    result = []
    result2 = []


    for i in range(1, 143):
        for j in range(1, 143):
            if my_value(j, i) == p:
                result.append(i)
                result.append(j)

            if my_value(j, i) == q:
                result2.append(i)
                result2.append(j)


    c = [0, 0]
    c[0] = result[0] + result2[0]
    c[1] = result[1] + result2[1]
    #
    # print(c)
    print("#{} {}".format(tc+1, int(my_value(c[1], c[0]))))



