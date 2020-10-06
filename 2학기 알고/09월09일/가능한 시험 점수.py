import sys
sys.stdin = open('가능한 시험 점수.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    digits = list(map(int, input().split()))

    used = [0]
    used2 = [0] * (sum(digits) + 1)
    used2[0] = 1

    for i in digits:
        for j in used[::-1]:
            print(j)
            if used2[j + i] != 1:
                used.append(j + i)
                used2[j + i] = 1

    print("#{} {}".format(tc + 1, len(used)))


