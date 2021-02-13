# from itertools import product

N, M = map(int, input().split())

def solution(N, M, cnt, result, idx):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, N + 1):
        result.append(i)
        solution(N, M, cnt + 1, result, i)
        result.pop()


solution(N, M, 0, [], 1)

'''
data = list(map(str, range(1, N + 1)))
print(data)
print(*list(map(' '.join, product(data, repeat=M))), sep='\n')
# for i in product(data, repeat=M):
#     print(*i)
'''
