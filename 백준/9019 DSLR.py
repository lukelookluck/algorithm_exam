from collections import deque
import sys


def D(n):
    return 2*n % 10000, 'D'


def S(n):
    return (n - 1) % 10000, 'S'


def L(n):
    return (n % 1000) * 10 + n // 1000, 'L'


def R(n):
    return (n % 10) * 1000 + n // 10, 'R'


def find(n):
    answer = ''
    while n != A:
        answer = route[n] + answer
        n = check[n]
    print(answer)


T = int(sys.stdin.readline().strip())
for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    check = [-1] * 10000
    route = [''] * 10000
    temp = deque([A])

    while temp:
        a = temp.popleft()

        if a == B:
            find(a)
            break

        for i, j in (D(a), S(a), L(a), R(a)):
            if check[i] == -1:
                check[i] = a
                route[i] = j
                if i == B:
                    temp.appendleft(i)
                else:
                    temp.append(i)


