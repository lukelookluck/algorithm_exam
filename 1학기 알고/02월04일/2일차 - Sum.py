import sys
sys.stdin = open('a.txt', 'r')

def r_c_max_sum(arr):
    max_value = 0
    for i in range(len(arr)):
        row_sum = 0
        column_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
            column_sum += arr[j][i]
        if row_sum > max_value and row_sum >column_sum:
            max_value = row_sum
        elif column_sum > max_value and column_sum > row_sum:
            max_value = column_sum
    return max_value

def diagonal_sum(arr):
    for i in range(len(arr)):
        diagonal_sum = 0
        reverse_sum = 0
        for j in range(len(arr)):
            diagonal_sum += arr[i][j]
            reverse_sum += arr[i][len(arr)-1-j]
        if diagonal_sum > reverse_sum:
            return diagonal_sum
        else:
            return reverse_sum

T = 10
for tc in range(T):
    iteration = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
            arr[i] = list(map(int, input().split()))

    #time
    a = r_c_max_sum(arr)
    b= diagonal_sum(arr)
    if a > b:
        print('#{} {}'.format(tc + 1, a))
    else:
        print('#{} {}'.format(tc + 1, b))