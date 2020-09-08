import sys
sys.stdin = open('a.txt')

def binarySearch(E, K):
    start = 1
    end = E
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == K:
            return count
        elif middle > K:
            end = middle
        else:
            start = middle
    return count

T = int(input())
for tc in range(T):
    E, A, B = map(int, input().split())
    result_A = binarySearch(E, A)
    result_B = binarySearch(E, B)
    # print(result_A)
    # print(result_B)
    if result_A < result_B:
        print("#{} {}".format(tc+1, "A"))
    elif result_A == result_B:
        print("#{} {}".format(tc + 1, 0))
    else:
        print("#{} {}".format(tc + 1, "B"))
