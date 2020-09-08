import sys
sys.stdin = open('가능한 시험 점수.txt')

#
# def my_func(n, i, my_sum):
#     global count
#     if i == n:
#         if my_sum not in result:
#             result.append(my_sum)
#             count += 1
#         return
#     else:
#         my_func(n, i+1, my_sum+digits[i])
#         my_func(n, i+1, my_sum)


T = int(input())
for tc in range(T):
    N = int(input())
    digits = list(map(int, input().split()))
    used = [0] * (sum(digits) + 1)
    used[0] = 1
    count = 1
    for i in digits:
        for j in range(len(used)-1, -1, -1):
            if used[j] == 1 and used[i + j] != 1:
                used[i + j] = 1
                count += 1

    print("#{} {}".format(tc+1, count))

