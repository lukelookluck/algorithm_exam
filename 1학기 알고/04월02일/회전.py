import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    my_digit = M % N
    print("#{} {}".format(tc+1, arr[my_digit]))
