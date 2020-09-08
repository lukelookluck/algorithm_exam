import sys
sys.stdin = open('홀수만 더하기.txt')

T = int(input())
for tc in range(T):
    data = [*map(int, input().split())]
    result = 0
    for i in data:
        if i % 2:
            result += i
    print("#{} {}".format(tc+1, result))