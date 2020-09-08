import sys
sys.stdin = open('평균값 구하기.txt')

for tc in range(int(input())):
    data = [*map(int, input().split())]
    sum = 0
    for i in data:
        sum += i
    result = sum / 10
    print("#{} {}".format(tc+1, round(result)))
