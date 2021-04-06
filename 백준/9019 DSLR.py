from collections import deque
import sys


def D(n):
    n *= 2
    if n > 9999:
        return [n % 10000, 'D']
    return [n, 'D']


def S(n):
    if n == 0:
        return [9999, 'S']
    return [n - 1, 'S']


def L(n):
    return [(n % 1000) * 10 + n // 1000, 'L']


def R(n):
    return [(n % 10) * 1000 + n // 10, 'R']


def find(n):
    answer = ''
    while n != A:
        answer = check[n][1] + answer
        n = check[n][0]
    print(answer)


# pypy로만 통과함
T = int(sys.stdin.readline().strip())
for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    check = [0] * 10000

    temp = deque([A])

    while temp:
        # print(check)
        # print(temp)
        a = temp.popleft()

        if a == B:
            find(a)
            break

        for i in (D(a), S(a), L(a), R(a)):
            # print(i)
            if not check[i[0]]:
                check[i[0]] = [a, i[1]]
                temp.append(i[0])


