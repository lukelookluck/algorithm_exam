h, m = map(int, input().split())

t_m = h * 60 + m - 45

if t_m < 0:
    t_m += 1440

print(t_m // 60, t_m % 60)