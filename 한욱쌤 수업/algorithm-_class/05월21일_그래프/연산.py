import sys
sys.stdin = open('연산.txt')

# deque 사용을 위해 import
from collections import deque


def my_func(num2):
    global result
    result = 0
    while my_queue:
        # deque 리스트 맨 앞에꺼 하나 빼오기
        temp_digit, cnt = my_queue.popleft()
        # 그게 찾는 값이면 cnt 값 리턴, 종료
        if temp_digit == num2:
            return cnt

        # 제약조건에 안 걸리고 이미 나온 숫자가 아니면, visit에 체크하고 deque 리스트에 삽입
        if temp_digit + 1 <= 1000000 and not visit[temp_digit + 1]:
            visit[temp_digit + 1] = 1
            my_queue.append((temp_digit + 1, cnt + 1))
        if temp_digit - 1 >= 0 and not visit[temp_digit - 1]:
            visit[temp_digit - 1] = 1
            my_queue.append((temp_digit - 1, cnt + 1))
        if temp_digit * 2 <= 1000000 and not visit[temp_digit * 2]:
            visit[temp_digit * 2] = 1
            my_queue.append((temp_digit * 2, cnt + 1))
        if temp_digit - 10 >= 0 and not visit[temp_digit - 10]:
            visit[temp_digit - 10] = 1
            my_queue.append((temp_digit - 10, cnt + 1))


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # (2,0) 앞에꺼 숫자, 뒤에꺼 연산 수(=cnt)
    my_queue = deque([(N, 0)])
    visit = [0] * 1000001
    print("#{} {}".format(tc+1, my_func(M)))
