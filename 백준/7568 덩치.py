N = int(input())
my_list = []
for i in range(N):
    my_list.append(list(map(int, input().split())))
check = [1 for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if my_list[i][0] > my_list[j][0] and my_list[i][1] > my_list[j][1]:
            check[j] += 1
        elif my_list[i][0] < my_list[j][0] and my_list[i][1] < my_list[j][1]:
            check[i] += 1

print(*check)