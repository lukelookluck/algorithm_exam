import sys

T = int(sys.stdin.readline())
for t in range(T):
    data = sys.stdin.readline().strip()
    cnt = 0
    for dt in data:
        if dt == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')
