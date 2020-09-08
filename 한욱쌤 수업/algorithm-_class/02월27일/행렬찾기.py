import sys
sys.stdin = open('행렬찾기.txt')

# def my_func(fr, fc):


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split() + [0])) for _ in range(N)] +[[0]*(N+1)]
    # print(arr)
    result_count = 0
    result_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                set_column = j
                set_row = i
                count_column = 0
                count_row = 0
                while arr[i][j] != 0 and j != N:
                    arr[i][j] = 0
                    j += 1
                    count_column += 1
                i = set_row
                j = set_column
                arr[i][j] = 1
                while arr[i][j] != 0 and i != N:
                    arr[i][j] = 0
                    i += 1
                    count_row += 1
                # print(count_column)
                # print(count_row)
                result_list += [count_row, count_column]
                # print("===")
                i = set_row
                j = set_column
                # print("~~~")
                # print(arr)
                for k in range(count_row):
                    for m in range(count_column):
                        arr[i+k][j+m] = 0
                # print(arr)
                result_count += 1
    # print(result_count)
    # print(result_list)
    result = []
    used = []
    while len(result) != len(result_list):
        my_min = float('inf')
        for i in range(0, len(result_list), 2):
            if i not in used:
                if my_min > (result_list[i] * result_list[i + 1]):
                    my_min = (result_list[i] * result_list[i + 1])
                    my_value = result_list[i]
                    my_digit = i
                if my_min == (result_list[i] * result_list[i + 1]):
                    if result_list[i] < result_list[my_digit]:
                        my_digit = i
        used += [my_digit]
        result += [result_list[my_digit], result_list[my_digit + 1]]
    # print(used)
    # print(result)

    print("#{}".format(tc+1), end= ' ')
    print(result_count, end= ' ')
    print(*result)


