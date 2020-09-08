def fac(int):
    while int > 0:
        return int * fac(int - 1)
    if int == 0:
        return 1

print(fac(5))
print(fac(4))
print(fac(3))
print(fac(2))
print(fac(1))
print(fac(0))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(4))
# print(fact(1))
# print(fact(0))