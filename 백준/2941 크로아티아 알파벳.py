data = input()
check = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ans = 0

for c in check:
    ans += data.count(c)
    data = data.replace(c, ' ')

for i in data.split():
    ans += len(i)
print(ans)