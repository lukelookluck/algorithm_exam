import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt')

def my_func(i, j, count):
    global my_str
    my_str.append(str(arr[i][j]))
    if count == 7:
        result.add(''.join(my_str))
        return
    for k in range(4):
        if 0 <= i+dx[k] < 4 and 0 <= j+dy[k] < 4:
            my_func(i+dx[k], j+dy[k], count+1)
            my_str.pop()


T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    print(arr)
    result = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            my_str = []
            my_func(i, j, 1)
    print("#{} {}".format(tc+1, len(result)))
