import sys

def solution(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = solution(arr[:mid])
    high_arr = solution(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


N = int(sys.stdin.readline())
data = []
for n in range(N):
    data.append(int(sys.stdin.readline()))


print(*solution(data), sep='\n')

# print(*sorted(data), sep='\n')