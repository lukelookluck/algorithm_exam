from collections import deque
import sys


def search(x):
    answer = ''
    for _ in range(check[x] + 1):
        answer = f'{x} {answer}'
        x = move[x]
    print(answer)


def solution(N, K):
    temp = deque([N])

    while temp:
        x = temp.popleft()
        if x == K:
            print(check[x])
            search(x)
            return

        for new_x in (x*2, x+1, x-1):
            if 0 <= new_x <= 100000 and not check[new_x]:
                temp.append(new_x)
                check[new_x] = check[x] + 1
                move[new_x] = x


N, K = map(int, sys.stdin.readline().split())
check = [0] * 100001
move = [0] * 100001
solution(N, K)