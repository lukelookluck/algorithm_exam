case1 = "()()((()))"
case2 = "((()((((()()((()())((()))))))))))))))))))"
case3 = "((("

def my_verify(data):
    count_1 = 0
    count_2 = 0
    for i in data:
        if i == "(":
            count_1 += 1
        elif i == ")":
            count_2 += 1

    if count_1 == count_2:
        return "짝이 맞습니다."
    else:
        if count_1 > count_2:
            return ") 의 갯수가 {}개 부족합니다.".format(count_1 - count_2)
        else:
            return "( 의 갯수가 {}개 부족합니다.".format(count_2 - count_1)

print(my_verify(case1))
print(my_verify(case2))
print(my_verify(case3))