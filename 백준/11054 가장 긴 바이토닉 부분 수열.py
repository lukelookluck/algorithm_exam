import sys


def solution():
    for i in range(N):
        for j in range(i, N):
            if arr[i] < arr[j] and check2[i] >= check2[j]:
                check2[j] += 1
            if arr[-i - 1] < arr[-j - 1] and check[-i - 1] >= check[-j - 1]:
                check[-j - 1] += 1

    for i in range(N):
        check[i] += check2[i] - 1

    return max(check)


N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
check = [1] * N
check2 = [1] * N

print(solution())