N = int(input())
ans = 0

for n in range(N):
    data = input()
    data = '!' + data
    result = ''
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            result += data[i]
    my_bool = True

    for r in result:
        if result.count(r) > 1:
            my_bool = False
            break

    if my_bool:
        ans += 1

print(ans)
