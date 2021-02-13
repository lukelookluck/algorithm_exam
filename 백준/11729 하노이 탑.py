def solution(n, start, end):
    if n == 1:
        print(start, end)
        return

    solution(n - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    solution(n - 1, 6 - start - end, end)  # 3단계


N = int(input())
print(2 ** N - 1)
solution(N, 1, 3)