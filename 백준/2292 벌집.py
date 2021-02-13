import math
N = int(input())

ans = -1 + ((4 * N - 1) / 3)**(1/2)
print(math.ceil(ans/2) + 1)