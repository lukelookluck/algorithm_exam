import sys
sys.stdin = open('컨테이너 운반.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    wi = sorted([*map(int, input().split())], reverse=True)
    ti = sorted([*map(int, input().split())], reverse=True)
    result = 0
    # print(wi, ti)
    for i in wi:
        for j in ti:
            if j >= i:
                result += i
                # wi.remove(i)
                ti.remove(j)
                break
    print("#{} {}".format(tc+1, result))