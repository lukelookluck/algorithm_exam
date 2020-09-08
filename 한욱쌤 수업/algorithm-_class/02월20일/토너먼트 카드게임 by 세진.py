def GBB(s, e):
    if s == e:
        return s
    m1 = GBB(s, (s+e)//2)
    m2 = GBB((s+e)//2 + 1, e)
    if (lis[m2] == 1 and lis[m1] == 3 or
        lis[m2] == 2 and lis[m1] == 1 or
        lis[m2] == 3 and lis[m1] == 2):
        return m2
    else:
        return m1

T = int(input())
for tc in range(T):
    N = int(input())
    lis = list(map(int, (('0 ' + input())).split()))

    print("#{} {}".format(tc+1, GBB(1, N)))