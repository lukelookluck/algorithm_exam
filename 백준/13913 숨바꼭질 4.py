from collections import deque
import sys


def search(x):
    answer = []
    while x != N:
        answer.append(x)
        x = move[x]
    answer.append(N)
    answer.reverse()
    print(*answer)
    return


def solution(N, K):
    temp = deque([N])
    while temp:
        x = temp.popleft()
        if x == K:
            print(check[x])
            search(x)
            return

        for new_x in (x+1, x-1, x*2):
            if 0 <= new_x <= 100000 and not check[new_x]:
                temp.append(new_x)
                check[new_x] = check[x] + 1
                move[new_x] = x


N, K = map(int, sys.stdin.readline().split())
check = [0] * 100001
move = [0] * 100001
solution(N, K)