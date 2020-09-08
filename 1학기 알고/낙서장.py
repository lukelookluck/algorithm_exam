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
my_cnt = 0
my_odd, my_even = 0, 0
my_result = 0
zzz = 0
i = '1FF1F8FC01C7FF8E3FE3F1F8038FFF1C01F8E00FC7'
my_decimal = int(i, 16)
my_bin_length = round((4 * len(i) / 56))
# print(len(i))
# print(my_bin_length)
my_bin = format(int(i, 16), 'b').zfill((my_bin_length * 56) + 3).rstrip('0')
print(my_bin)
my_index = 0
my_count = 0
my_digit = '1'
my_list = []
N = my_bin_length
asb = ''
for j in my_bin[-1:-56 * N - 1:-1]:
    if j == my_digit:
        my_index += 1
    elif j != my_digit:
        my_list.append(my_index // N)
        my_digit = j
        my_index = 1
    my_count += 1
    # print(my_list)
    # print("N", N)
    if my_count == 7 * N:
        my_list.append(my_index // N)
        # print(my_count)
        # print(my_list)
        my_count = 0

        for keys, values in my_keys.items():
            if values == my_list:
                # print("MY_CNT", my_cnt)
                if my_cnt % 2:
                    my_odd += int(keys)
                    print(my_odd)
                else:
                    # print("!@#awdnasjndaslk")
                    my_even += int(keys)
                    print("even", my_even)
                # 결과값 도출을 위해 각 칸의 키값을 my_result에 합산
                print(my_list, keys)
                asb += keys
                my_result += int(keys)

        my_cnt += 1
        my_list = []
        my_digit, my_index = '1', 0
        if ((my_odd * 3) + my_even) % 10 == 0:
            print("{} {}".format(zzz + 1, asb), i, my_result)
            zzz += 1
asb = ''