import sys
sys.stdin = open('a.txt')

T = int(input())
# arr = [[0 for _ in range(10)] for _ in range(10)]
for tc in range(T):
    N = int(input())
    result = 0
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for num in range(N): # 1233/3668/2356
        fc, fr, lc, lr, c = map(int, input().split())
        # print(fc)
        # print(fr)
        # print(lc)
        # print(lr)
        # print("---------------------------")
        for i in range(fc, lc+1): # 1, 2, 3
            for j in range(fr, lr+1): # 2, 3
                # print(i)
                # print(j)
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                arr[i][j] += c
                # print(arr[i][j])
                # print("=======================================")
    # print(arr)
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                result += 1
        # result = arr.count(3)

    print("#{} {}".format(tc+1, result))