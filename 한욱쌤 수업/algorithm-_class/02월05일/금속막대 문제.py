import sys
sys.stdin = open('a.txt')

def divide_list(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

T = int(input())
for tc in range(T):
    numbers = int(input())
    data = list(map(int, input().split()))
    result = []
    # print(data)

    divided_list = list(divide_list(data, 2))
    print(divided_list)
    # print(divided_list[0])
    # print(divided_list[0][0])

    for i in data:
        for j in range(0, len(data), 2):
            if data.count(i) == 1 and data[j] == i:
                one_num = i
    # print("one_num: {}".format(one_num))

    for k in range(len(divided_list)):
        if divided_list[k][0] == one_num:
            break
    result.append(divided_list[k][0])
    result.append(divided_list[k][1])
    # print(result)

    for i in range(numbers):
        for j in range(numbers):
            if result[-1] == divided_list[j][0]:
                result.append(divided_list[j][0])
                result.append(divided_list[j][1])
                # print(result)
    # list에서 [] 제거하는 코드
    print("#{}".format(tc+1), *result)
    print("#{} {}".format(tc+1, ' '.join(map(str,result))))
            #
    # divided_list[0], divided_list[k] = divided_list[k], divided_list[0]
    # print(divided_list)

    # for i in range(0, numbers - 1):
    #     same = i
    #     for j in range(i+1, numbers):
    #         # for k in range(divided_list[min]):
    #         if divided_list[same][k] ==



