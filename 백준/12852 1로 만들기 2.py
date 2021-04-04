import sys


def solution1(x, data, cnt):
    global answer_cnt, answer
    # print(x, data, cnt)

    if cnt >= answer_cnt:
        return

    if x == 1:
        # print('??')
        if answer_cnt > cnt:
            answer_cnt = cnt
            answer = data
            # print(data)
        return

    if not x % 3:
        solution1(x // 3, data + [x // 3], cnt + 1)
    if not x % 2:
        solution1(x // 2, data + [x // 2], cnt + 1)
    solution1(x - 1, data + [x - 1], cnt + 1)


N = int(sys.stdin.readline().strip())
answer_cnt = 1000000
answer = []
solution1(N, [N], 0)
print(answer_cnt)
print(*answer)