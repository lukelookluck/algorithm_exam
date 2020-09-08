def my_strrev(a):
    result = list(a)
    result2 = []
    for i in range(len(result)-1, len(result)//2 -1, -1):
        result2.append(result[i])
    for j in range(len(result)//2 -1, -1, -1):
        result2.append(result[j])
    return ''.join(result2)




a = 'qwerty'
# b = list(a)
# c = []
# for i in range(len(a)-1, len(a)//2-1, -1):
#     print(b[i])
# print(my_strrev(a))
b = [a]
print(b)
print(''.join(a[::-1]))


