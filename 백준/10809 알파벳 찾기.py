data = input()

for i in range(97, 123):
    my_bool = True
    for n, j in enumerate(data):
        if j == chr(i):
            my_bool = False
            print(n, end=' ')
            break
    if my_bool is True:
        print(-1, end=' ')
