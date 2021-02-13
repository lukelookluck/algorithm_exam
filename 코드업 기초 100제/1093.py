n = int(input())
arr = list(map(int, input().split()))

my_list = [0] * 23
for i in arr:
    my_list[i-1] += 1

print(*my_list)