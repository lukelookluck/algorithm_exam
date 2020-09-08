import sys
sys.stdin = open('토너먼트 카드게임.txt')

def my_func(fn, ln):
    if fn == ln:
        return fn

    set_num1 = my_func(fn, (fn+ln)//2)
    set_num2 = my_func((fn+ln)//2 + 1, ln)

    if (data[set_num2] == 2 and data[set_num1] == 1 or
        data[set_num2] == 3 and data[set_num1] == 2 or
        data[set_num2] == 1 and data[set_num1] == 3):
        return set_num2
    else:
        return set_num1

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    print("#{} {}".format(tc+1, my_func(0, N-1)+1))

