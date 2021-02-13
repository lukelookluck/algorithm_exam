def solution(n):
    my_list = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            my_list.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            my_list.append(n[i % len(n)] * 3)
    return my_list


N = int(input())
ans = ["***", "* *", "***"]
cnt = 0
while N != 3:
    N = N // 3
    cnt += 1

for i in range(cnt):
    ans = solution(ans)
for i in ans:
    print(i)