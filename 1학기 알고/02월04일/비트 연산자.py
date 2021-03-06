arr = [1, 2, 3]

n = len(arr) # 3

for i in range(1<<n):  # 0 ~ 7, 총 8개  부분 집합의 개수
    for j in range(n): # j = 0, 1, 2  원소의 수 만큼 비트 비교
        if i & (1<<j): # i의 j 번째 비트가 1이면 j번째 원소를 출력
            print(arr[j], end=" ")
    print()
print()

"""
0 - 000 {}
1 - 001 {1}
2 - 010 {2}
3 - 011 {1, 2}
4 - 100 {3}
5 - 101 {1, 3}
6 - 110 {2, 3}
7 - 111 {1. 2. 3}
"""