import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt')

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i:],r-1):
                yield [arr[i]] + next


T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # print(arr)
    result = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]



    for i in range(4):
        for j in range(4):
            for k in combinations([0, 1, 2, 3], 6):
                my_str = []
                my_str.append(str(arr[i][j]))
                for m in k:
                    my_str.append(str(arr[i+dx[m]]))

    print("#{} {}".format(tc+1, len(result)))
