from collections import deque


def posible_spot(cur1, cur2, new_board):
    spots = []
    # 평행 탐색
    dy_dx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    print('cur1, cur2', cur1, cur2)
    for dy, dx in dy_dx:
        nxt1 = (cur1[0] + dy, cur1[1] + dx)
        nxt2 = (cur2[0] + dy, cur2[1] + dx)
        if new_board[nxt1[0]][nxt1[1]] == 0 and new_board[nxt2[0]][nxt2[1]] == 0:
            print(nxt1, nxt2)
            spots.append((nxt1, nxt2))
            print(spots)
    # 회전 탐색
    derection = [-1, 1]
    if cur1[0] == cur2[0]:  # 가로방향 일 때
        for d in derection:
            if new_board[cur1[0] + d][cur1[1]] == 0 and new_board[cur2[0] + d][cur2[1]] == 0:
                spots.append((cur1, (cur1[0] + d, cur1[1])))
                spots.append((cur2, (cur2[0] + d, cur2[1])))
                print('spots', spots)

    else:  # 세로 방향 일 때
        for d in derection:
            if new_board[cur1[0]][cur1[1] + d] == 0 and new_board[cur2[0]][cur2[1] + d] == 0:
                spots.append(((cur1[0], cur1[1] + d), cur1))
                spots.append(((cur2[0], cur2[1] + d), cur2))

    return spots


def solution(board):
    # board 외벽 둘러싸기
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]
    for i in new_board:
        print(*i)
    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for spot in posible_spot(cur1, cur2, new_board):
            if spot not in confirm:
                que.append((*spot, count + 1))
                confirm.add(spot)

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
step = [(0, 0), (0, 1)]

print(solution(board))
