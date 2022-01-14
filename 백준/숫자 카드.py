import sys

n = int(input())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(n, n_arr, m, m_arr):
    answer = []
    n_arr = sorted(n_arr)
    my_min, my_max = n_arr[0], n_arr[-1]

    for x in m_arr:
        if x > my_max or x < my_min:
            answer.append(0)
        else:
            my_bool = True
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if x > n_arr[mid]:
                    left = mid + 1
                else:
                    if x == n_arr[mid]:
                        my_bool = False
                    right = mid - 1
            if my_bool:
                answer.append(0)
            else:
                answer.append(1)
    print(*answer)


solution(n, n_arr, m, m_arr)

