X =int(input())
key, my_se = 0, 1
while key < X:
    key += my_se
    my_se += 1

df = key - X
if (my_se-1) % 2:
    print(str(1 + df) + '/' + str(my_se-1 - df))
else:
    print(str(my_se - 1 - df) + '/' + str(1 + df))