import sys
sys.stdin = open('미로1.txt')

T = 10
for tc in range(T):
    a = input()
    # 주어진 데이터로 배열 만들기
    arr = [list(map(int, input())) for _ in range(16)]
    # 방문 배열 만들기
    visited = [[0 for _ in range(16)] for _ in range(16)]
    answer = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    #  스택에 시작 뿌리 저장
    my_stack = [(1, 1)]

    while my_stack:
        # 스택에서 1개 pop해서 x, y로 저장
        x, y = my_stack.pop()
        for i in range(4):
            # 상하좌우 보기
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 그 중 출구라면 ㅅㄱ
            if arr[next_x][next_y] == 3:
                answer = 1
                break

            # 벽이 아니라면
            if not visited[next_x][next_y] and not arr[next_x][next_y]:
                # 방문한 거에 찍고
                visited[next_x][next_y] = 1
                # 스택에 저장
                my_stack.append((next_x, next_y))

    print("#{} {}".format(tc+1, answer))
