n = int(input())

my_arr = [[0]*19 for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    my_arr[x-1][y-1] = 1

for i in range(19):
    print(*my_arr[i])
