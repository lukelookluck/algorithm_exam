my_arr = list(map(int, input().split()))
n = 1
for i in my_arr:
    n *= i

n = n / 8 / 1024 / 1024
print('%.1f' %n, 'MB')
