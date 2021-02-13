N = int(input())
ans_list = [666]
cnt = 1
i = 1666
while cnt != N:
    if '666' in str(i) or '6666' in str(i):
        ans_list.append(i)
        cnt += 1
    i += 1

print(ans_list[N-1])