from collections import deque
import sys
sys.stdin = open('Contact.txt')


def my_func(my_stack):
    global answer

    my_stack2 = []

    # 이번에 방문할 뿌리들에서 1개씩 뽑기
    for i in my_stack:
        # 그게 방문한 거면 통과
        if i in visited:
            continue
        # 방문한 걸로 저장
        visited.append(i)
        # 그게 나무의 키에 있다면(요거 없으면 키에러남)
        if i in my_list:
            # 그 키의 값들을 돌며 1개씩 뽑기
            for j in my_list[i]:
                # 그게 방문한 거면 통과
                if j in visited:
                    continue
                # 다음에 방문할 뿌리로 저장
                my_stack2.append(j)

    if my_stack2:
        # 다음에 방문할 뿌리를 이번에 방문할 뿌리로 저장
        my_stack = my_stack2
        # 재귀 ㄱㄱ
        my_func(my_stack)
    else:
        # 다음에 방문할 뿌리들이 없다면 이번에 방문할 뿌리들 중 큰 값이 정답
        answer = max(my_stack)

T = 2
for tc in range(T):
    n, root = map(int, input().split())
    digits = list(map(int, input().split()))
    print(digits)
    my_list = {}
    answer = 0

    # 방문 리스트
    visited = []

    # 시작 뿌리 설정
    my_stack1 = [root]

    # 주어진 값들을 딕셔너리(aka 나무)로 만들기
    for i in range(0, n, 2):
        if digits[i] in my_list:
            my_list[digits[i]] += [digits[i + 1]]
        else:
            my_list[digits[i]] = [digits[i+1]]
    print(my_list)

    my_func(my_stack1)
    print(answer)