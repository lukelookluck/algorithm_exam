def solution(numbers, target):
    answer = 0

    def dfs(idx, my_sum):
        if idx == len(numbers):
            if my_sum == target:
                nonlocal answer
                answer += 1
            return

        dfs(idx + 1, my_sum + numbers[idx])
        dfs(idx + 1, my_sum - numbers[idx])

    dfs(0, 0)

    return answer


n = [1, 1, 1, 1, 1]
t = 3
solution(n, t)
