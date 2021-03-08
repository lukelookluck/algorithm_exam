from collections import Counter
import sys


def solution(arr, middle):
    result = 0
    for each, cnt in arr.items():
        if each > middle:
            result += (each - middle) * cnt

        if result >= M:
            break
    return result


N, M = map(int, sys.stdin.readline().split())
my_arr = Counter(map(int, sys.stdin.readline().split()))

start, end = 0, max(my_arr)

while start <= end:
    my_middle = (start + end) // 2

    if solution(my_arr, my_middle) >= M:
        start = my_middle + 1
    else:
        end = my_middle - 1

print(end)