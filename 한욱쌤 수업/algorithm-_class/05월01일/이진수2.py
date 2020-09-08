import sys
sys.stdin = open('이진수2.txt')

def my_def(mG, cnt):
    global my_result
    # print(mG)
    if cnt == 13:
        my_result = 'overflow'
        return
    if mG > 0:
        mG = mG * 2
        # print(mG)
        if mG >= 1:
            my_result += "1"
            # print(my_result)
            my_def(mG-1, cnt + 1)
        else:
            my_result += "0"
            my_def(mG, cnt + 1)

    else:
        return


T = int(input())
for tc in range(T):
    N = float(input())
    my_result = ""
    my_def(N, 0)
    print("#{} {}".format(tc+1, my_result))