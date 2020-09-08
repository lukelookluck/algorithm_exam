import sys
sys.stdin = open('영준이의 카드 카운팅.txt')

def divide_list(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

T = int(input())
for tc in range(T):
    data = input()
    data1 = ''
    li = list()
    # print(data)
    count_s = 0
    count_d = 0
    count_h = 0
    count_c = 0
    for i in range(int(len(data) / 3)):
        data1 = data[3 * i : 3 * (i + 1)]
        li.append(data1)
    # print(li)

    for i in range(len(li)):
        nabreak = True

        # print(li[i][0])
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                result = ["ERROR"]
                nabreak = False
                break
        if nabreak == False:
            break

        if li[i][0] == "S":
            count_s += 1
        if li[i][0] == "D":
            count_d += 1
        if li[i][0] == "H":
            count_h += 1
        if li[i][0] == "C":
            count_c += 1
    else:
        result = [13-count_s, 13-count_d, 13-count_h, 13-count_c]
        # print(result)
        # print(count_s)
        # print(count_d)
        # print(count_h)
        # print(count_c)

    print("#{} {}".format(tc+1, ' '.join(map(str,result))))

    # print(data[:3])
    #
    # for i in range(0, len(data)-1, 3):
    #     print(data[i+1] + data[i+2])