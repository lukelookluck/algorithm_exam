import sys

N = int(sys.stdin.readline())
my_arr = [0] * 10001

for n in range(N):
    my_arr[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(my_arr[i]):
        print(i)