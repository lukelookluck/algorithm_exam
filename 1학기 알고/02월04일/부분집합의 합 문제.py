import sys
sys.stdin = open('a.txt', 'r')
arr = list(range(1, 13))
T = int(input())


# def subset_sum(arr):

        #         if subset_sum == K:
        #             return print(arr[j], end=" ")

for tc in range(T):
    N, K= map(int, input().split())
    len_arr = len(arr)
    count = 0

    for i in range(1, 1<<len_arr):
        subset_sum = 0
        result = []

        for j in range(len_arr):

            if i & (1<<j):
                subset_sum += arr[j]
        if subset_sum == K:

            for j in range(len_arr):
                if i & (1 << j):
                    result.append(arr[j])
            if (len(result)) == N:
                # print(result)
                count += 1
                # print(count)

    print("#{} {}".format(tc+1 , count))

    # print(subset_sum(arr))
