a, b = input().split()
r_a, r_b = int(a[::-1]), int(b[::-1])
if r_a > r_b:
    print(r_a)
else:
    print(r_b)