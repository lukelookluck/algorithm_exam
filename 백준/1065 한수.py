def solution(n):
    str_n = str(n)
    df1 = int(str_n[0]) - int(str_n[1])
    df2 = int(str_n[1]) - int(str_n[2])

    if df1 == df2:
        return True
    else:
        return False


N = int(input())
cnt = 0

for i in range(1, N+1):
    if i < 100:
        cnt += 1
    else:
        if solution(i):
            cnt += 1

print(cnt)