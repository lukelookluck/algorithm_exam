def comb(idx, cnt):
    if cnt == 2:
        print(a)
        return
    if a:
        start = a[-1]
    else:
        start = 0
    for i in range(start, 4):
        if lis[i] not in a:
            a.append(lis[i])
            comb(idx + 1, cnt + 1)
            a.pop()
lis = [1, 2, 3, 4]
a = []
for i in range(1):
    comb(0, 0)