def solution(rows, columns, queries):
    answer = []
    table = [[0 for col in range(columns + 1)] for row in range(rows + 1)]
    t = 1
    
    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            table[row][col] = t
            t += 1

    for x1, y1, x2, y2 in queries:
        init = table[x1][y1] # 왼쪽 위 값 저장
        my_min = init
        
        # left
        for i in range(x1 + 1, x2 + 1):
            table[i-1][y1] = table[i][y1]
            my_min = min(my_min, table[i][y1])
        # bottom
        for i in range(y1 + 1, y2 + 1):
            table[x2][i-1] = table[x2][i]
            my_min = min(my_min, table[x2][i])
        # right
        for i in range(x2 - 1, x1 - 1, -1):
            table[i+1][y2] = table[i][y2]
            my_min = min(my_min, table[i][y2])
        # top
        for i in range(y2 - 1, y1 - 1, -1):
            table[x1][i+1] = table[x1][i]
            my_min = min(my_min, table[x1][i])
            
        table[x1][y1+1] = init
        
        answer.append(my_min)

    return answer
