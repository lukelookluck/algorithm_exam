
T = int(input())
result = [(1, 0), (0, 1)]
cnt = 1


while cnt != 40:
    x, y = map(int, result[cnt-1])
    a, b = map(int, result[cnt])
    result.append((x+a, y+b))
    cnt += 1

for tc in range(T):
    N = int(input())
    print(*result[N])