arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len_arr = len(arr)
K = 10

for i in range(1, 1<<len_arr): #1 ~ 2**10 , 총 2*10개
    sum = 0
    for j in range(len_arr): #원소의 개수만큼(10개) 비교
        if i & (1 << j): # i의 j번째 비트가 1이면, j번째 원소 출력(이진법)
            sum += arr[j]  # j번째의 원소를 sum에 더함
        # print(sum)
    if sum == K:
        for j in range(len_arr):
            if i &(1 << j):
                print(arr[j], end = " ")
        print()