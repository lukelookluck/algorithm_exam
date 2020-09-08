def solution(clothes):
    # 부분집합 개수 구하는 공식 활용, 정답은 1로 초기화
    answer = 1
    # 각 의류당 개수 담을 딕셔너리
    my_clothes = {}

    # 이를테면 상의: 1, 하의: 2 일케 담김
    for i in clothes:
        if i[1] not in my_clothes:
            my_clothes[i[1]] = 1
        else:
            my_clothes[i[1]] += 1
    
    # 부분집합 구하는 공식 활용, 상의: 1, 하의: 2이면 부분집합 개수는 2*3로 6개
    for key, value in my_clothes.items():
        answer *= (value + 1)

    # 공집합 빼주기
    return answer - 1