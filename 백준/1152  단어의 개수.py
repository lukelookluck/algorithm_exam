data = input().strip()
if len(data) == 0:
    print(0)
else:
    print(data.count(' ') + 1)