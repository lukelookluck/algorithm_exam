a = int(input())

for i in range(1, a+1):
    if i % 3:
        print(i, end=' ')
    else:
        print('X', end=' ')

