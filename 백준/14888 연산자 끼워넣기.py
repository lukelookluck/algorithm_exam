import sys


def solution(cnt, result):
    if cnt == N:
        answer.append(result)
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                solution(cnt + 1, result + digits[cnt])
            elif i == 1:
                solution(cnt + 1, result - digits[cnt])
            elif i == 2:
                solution(cnt + 1, result * digits[cnt])
            else:
                if result < 0:
                    solution(cnt + 1, -(-result // digits[cnt]))
                else:
                    solution(cnt + 1, result // digits[cnt])
            operator[i] += 1


N = int(sys.stdin.readline())
digits = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
answer = []

solution(1, digits[0])
print(max(answer), min(answer), sep='\n')
