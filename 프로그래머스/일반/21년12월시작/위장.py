def solution(clothes):
    answer = 1
    my_clothes = {}
    for c in clothes:
        if c[1] not in my_clothes:
            my_clothes[c[1]] = 1
        else:
            my_clothes[c[1]] += 1

    for mc in my_clothes.values():
        answer *= (mc[0] + 2)

    return answer - 1