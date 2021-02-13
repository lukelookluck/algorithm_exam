data = input().upper()
check = []

for i in range(65, 96):
    check.append(data.count(chr(i)))

result = max(check)
if check.count(result) > 1:
    print('?')
else:
    print(chr(65 + check.index(result)))


