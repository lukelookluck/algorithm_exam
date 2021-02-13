
def solution(n):
    if len(n) < 2:
        n = '0' + n
    sec = int(n[0]) + int(n[1])
    n = n[1] + str(sec)[-1]
    return n


N = input()
init = int(N)
cnt = 0
while True:
    N = solution(N)
    cnt += 1
    if init == int(N):
        break

print(cnt)




