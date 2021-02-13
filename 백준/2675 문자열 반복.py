T = int(input())
for tc in range(T):
    R, S = map(str, input().split())
    answer = ''
    for s in S:
        answer += s * int(R)
    print(answer)
