N = int(input())
my_list = []

for n in range(N):
    my_list.append(int(input()))
    for i in range(len(my_list)):
        while i > 0 and my_list[i-1] > my_list[i]:
            my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
            i -= 1

print(*my_list, sep='\n')