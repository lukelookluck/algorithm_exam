# 지그재그 순회

arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# print(len(arr))  # 2
# print(len(arr[0]))  # 5

def zigzag(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            return arr[i][j + (len(arr[0]) - 1 - 2*j) * (i % 2)]

print(zigzag(arr))
