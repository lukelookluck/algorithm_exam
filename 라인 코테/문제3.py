
def calculate(n, cnt):
    global answer1, answer2
    print('n, cnt', n, cnt)
    n = str(n)

    if len(n) == 1:
        print('최종!!', n, cnt)
        if answer1 > cnt:
            answer1 = cnt
            answer2 = int(n)
        return

    for i in range(1, len(n)):
        print(n[0:i], n[i:len(n)])
        if (len(n[0:i]) > 1 and n[0:i][0] == '0') or (len(n[i:len(n)]) > 1 and n[i:len(n)][0] == '0'):
            print("유효하지않아~")
            continue
        else:
            calculate(int(n[0:i]) + int(n[i:len(n)]), cnt+1)


def solution(n):
    global answer1, answer2
    answer = []
    calculate(n, 0)
    answer.append(answer1)
    answer.append(answer2)
    print(answer)
    return answer

answer1 = float('inf')
answer2 = 0

n = 9
solution(n)

