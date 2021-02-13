N = int(input())

len_N = len(str(N))
if N - 10 * len_N < 0:
    start = 0
else:
    start = N - 10 * len_N

ans = []
for i in range(start, N):
    str_i = str(i)
    my_sum = i

    for s in str_i:
        my_sum += int(s)

    if my_sum == N:
        ans.append(i)

if ans:
    print(min(ans))
else:
    print(0)