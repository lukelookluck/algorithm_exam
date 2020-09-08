import sys
sys.stdin = open('보물상자 비밀번호.txt')



def my_func(i):
    global result
    for i in range(int(N/n)):
        result += [digits[n*i+j:n*i+j +n]]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    digits = str(input())
    n = int(N/4)
    digits += digits[0:n-1]
    result = []
    for j in range(n):
        my_func(j)
    result = sorted(set(result), reverse=True)
    print("#{} {}".format(tc+1, int('0x' + result[K-1], 16)))
