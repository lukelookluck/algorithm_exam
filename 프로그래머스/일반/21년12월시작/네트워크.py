def solution(n, computers):
    answer = 0
    check = [0] * n

    def dfs(idx):
        check[idx] = 1

        for i in range(n):
            if computers[idx][i] and not check[i]:
                dfs(i)

    for i in range(n):
        if not check[i]:
            answer += 1
            dfs(i)

    return answer


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])