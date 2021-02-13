a, m, d, n = map(int, input().split())

idx = 1

while idx < n:
    a *= m
    a += d
    idx += 1

print(a)