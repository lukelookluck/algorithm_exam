from collections import deque

def solution(board, moves):
    answer = 0
    my_stack = []
    n = len(board)
    
    my_arr = [deque() for _ in range(n)]    
    
    for i in range(n):
        for j in range(n):
            if board[j][i]:
                my_arr[i].append(board[j][i])
    
    for m in moves:
        if not my_arr[m-1]:
            continue
        else:
            x = my_arr[m-1].popleft()
            if my_stack and my_stack[-1] == x:
                my_stack.pop()
                answer += 1
            else:
                my_stack.append(x)
    
    return answer * 2
