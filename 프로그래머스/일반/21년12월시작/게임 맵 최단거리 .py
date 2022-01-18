from collections import deque


def solution(maps):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    len1, len2 = len(maps), len(maps[0])
    check = [[-1 for _ in range(len2)] for _ in range(len1)]
    my_d = deque()
    my_d.append([len1 - 1, len2 - 1])
    check[len1-1][len2-1] = 1

    def check1(x, y):
        # if문으로 종료지점 check할 필요 없음
        # if [x, y] == [0, 0]:
        #     return True
        
        for i in range(4):
            n_x, n_y = x + d[i][0], y + d[i][1]
            if 0 <= n_x < len1 and 0 <= n_y < len2:                
                if check[n_x][n_y] == -1 and maps[n_x][n_y]:
                    # 함수에 cnt로 개수를 세가면서 하기보다는 check에서 개수 처리하는게 더 빠름                    
                    check[n_x][n_y] = check[x][y] + 1
                    my_d.append([n_x, n_y])
    
    while my_d:
        a, b = my_d.popleft()
        answer = check1(a, b)
        
    return check[0][0]
        
    
