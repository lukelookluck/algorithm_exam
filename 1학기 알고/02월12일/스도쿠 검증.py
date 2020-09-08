import sys
sys.stdin = open('스도쿠 검증.txt')

T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(1, 10)]
    digit_list = list(range(1, 10))
    result = []
    result2 = 0

    # 가로
    for i in range(9):
        y = sorted(arr[i])
        if y == digit_list:
            ok = True
        else:
            ok = False
            result.append(0)
            break

    # 세로
    for i in range(9):
        y_list = []
        for j in range(9):
            # print(arr[j][i])
            y_list.append(arr[j][i])
        # print(y_list)
        y = sorted(y_list)
        if y == digit_list:
            ok = True
        else:
            ok = False
            result.append(0)
            break

    # 9칸
    for j in range(0, 3):
        y_list = []
        for k in range(3):
            for m in range(3):
                y_list.append(arr[3*j+k][3*j+m])

        # print(y_list)
        y = sorted(y_list)
        if y == digit_list:
            ok = True
        else:
            ok = False
            result.append(0)
            break

    if 0 in result:
        result2 = 0
    else:
        result2 = 1

    print("#{} {}".format(tc+1, result2))