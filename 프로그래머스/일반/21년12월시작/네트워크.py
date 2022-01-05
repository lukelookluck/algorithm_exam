

def solution(n, computers):
    answer = 0
    check = [0] * n

    def bfs(idx):
        print('idx', idx)
        check[idx] = 1
        print(check)
        for i in range(n):
            print('compu', computers[idx], i)
            if computers[idx][i] and not check[i]:
                print('bfs', i)
                bfs(i)


    print(check)
    for i in range(n):
        if not check[i]:
            answer += 1
            print('i', i)
            bfs(i)
    print(answer)
    return answer


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])