from itertools import permutations
T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    print(Map)

    res = float('inf')
    for i in permutations(range(N), N):
        temp = 0
        for a in range(N):
            temp += Map[a][i[a]]
            if temp >= res: break
        res = res if res < temp else temp

    print("#{} {}".format(tc + 1, res))