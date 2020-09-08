import sys
sys.stdin = open('Contact.txt')

def called(stack):
    global ans

    stack2 = []

    for i in stack:
        if i in used:
            continue
        used.append(i)

        for j in mang[i]:
            if j in used:
                continue
            stack2.append(j)

    if stack2:
        stack = stack2
        called(stack)

    else:
        ans = max(stack)


T = 1

for tc in range(T):
    n, st = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    stack1 = [st]
    used = []
    maxN = max(lst)

    mang = [[] for _ in range(maxN + 1)]

    for i in range(0, len(lst), 2):
        mang[lst[i]].append(lst[i + 1])

    called(stack1)

    print("#{} {}".format(tc + 1, ans))