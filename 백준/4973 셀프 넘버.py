def d(n):
    ans = int(n)
    for i in str(n):
        ans += int(i)
    return ans


check = [0] * 10000

for i in range(1, 10000):
    n = d(i)
    if n < 10000:
        check[n] = 1

for i in range(1, 10000):
    if check[i] == 0:
        print(i)
