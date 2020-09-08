import sys
sys.stdin = open('암호코드 스캔.txt')

def my_func():
    n = 0
    tem_bin = ''
    while n < len(my_str):
        # print(my_decimal)
        my_bin = format(int(my_str[n], 16), 'b').zfill(4)
        # print(my_bin)
        tem_bin += my_bin  # 이를 정답변수에 저장
        n += 1
    return tem_bin

b = []
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # print(N)
    arr = [str(input()) for _ in range(N)]
    # print(arr)

    # 암호 해석을 위한 디셔너리 설정
    my_keys = {
        '0': [1, 1, 2, 3],
        '1': [1, 2, 2, 2],
        '2': [2, 2, 1, 2],
        '3': [1, 1, 4, 1],
        '4': [2, 3, 1, 1],
        '5': [1, 3, 2, 1],
        '6': [4, 1, 1, 1],
        '7': [2, 1, 3, 1],
        '8': [3, 1, 2, 1],
        '9': [2, 1, 1, 3],
    }

    tem_list = []
    my_n = 0
    my_result2 = 0
    my_cnt, my_odd, my_even, my_result = 0, 0, 0, 0
    my_str, my_str2, my_str3, my_str4, my_str5 = '', '', '', '', ''
    for i in range(N):
        # print(arr[i])
        tem_str = arr[i].strip('0')
        if tem_str:
            for i in tem_str:
                if i is not '0':
                    my_str += i

                if i is '0' and my_str:
                    if my_str not in tem_list and len(my_str) >= 14:
                        tem_list.append(my_str)
                        my_str.replace(my_str[-1], '')


                        # print("> <", my_str)
            if my_str not in tem_list and len(my_str) >= 14:
                tem_list.append(my_str)

            my_n = 0
            my_str = ''
    print(tem_list)
    # for i in tem_list

    zzz = 0
    for i in tem_list:
        my_decimal = int(i, 16)
        my_bin_length = round((4 * len(i) / 56))
        # print(len(i))
        # print(my_bin_length)
        print(i)
        my_bin = format(int(i, 16), 'b').zfill((my_bin_length*56)+3).rstrip('0')
        print(my_bin)
        my_index = 0
        my_count = 0
        my_digit = '1'
        my_list = []
        N = my_bin_length
        asb = ''
        for j in my_bin[-1:-56*N - 1:-1]:
            if j == my_digit:
                my_index += 1
            elif j != my_digit:
                my_list.append(my_index//N)
                my_digit = j
                my_index = 1
            my_count += 1
            # print(my_list)
            # print("N", N)
            if my_count == 7*N:
                my_list.append(my_index//N)
                # print(my_count)
                # print(my_list)
                my_count = 0

                for keys, values in my_keys.items():
                    if values == my_list:
                        # print("MY_CNT", my_cnt)
                        if my_cnt % 2:
                            my_odd += int(keys)
                            # print(my_odd)
                        else:
                            # print("!@#awdnasjndaslk")
                            my_even += int(keys)
                            # print("even", my_even)
                        # 결과값 도출을 위해 각 칸의 키값을 my_result에 합산
                        print(my_list, keys)
                        asb += keys
                        my_result += int(keys)
                print(asb)

                my_cnt += 1
                my_list = []
                my_digit, my_index = '1', 0
            # if len(asb) == 8:

        if ((my_odd * 3) + my_even) % 10 == 0:
            # print("result", my_result)
            my_result2 += my_result
            if asb:
                b.append(asb)

            # print("{} {}".format(zzz + 1, asb), i)
            zzz += 1

        asb = ''
        my_result, my_even, my_odd = 0, 0, 0

    print("#{} {}".format(tc + 1, my_result2))
    print(b)






