import sys
sys.stdin = open('이진수.txt')

T = int(input())
for tc in range(T):
    N, my_str = map(str, input().split())   # 입력에 문자가 있기에 일단 문자로 입력 받기
    my_result = ''  # 정답변수 초기 설정

    my_decimal = int(my_str, 16)    # 우선 입력 받은 16진수 문자를 my_decimal에 10진수로 저장
    # print(my_decimal)
    my_bin = format(my_decimal, 'b').zfill(4*int(N))    # 그 10진수를 2진수로 변환하되 zfill를 사용해서 16진수 각 자리수를 4자리 2진수로 변환
    my_result += my_bin    # 이 값을 정답변수에 저장         # 처음엔 자릿수 설정을 위한 zfill를 설정 안 해서 답 6개만 맞았음
    print("#{} {}".format(tc+1, my_result))             # 그리하여 아래의 코드를 만들었고 정답을 맞췄음


"""
T = int(input())
for tc in range(T):
    N, my_str = map(str, input().split())
    n = 0
    my_result = ''
    # print(my_str)
    while n < int(N):
        my_decimal = int(my_str[n], 16)
        # print(my_decimal)
        my_bin = format(my_decimal, 'b').zfill(4)       # 위 코드와의 차이점은 사실상 없음 
        # print(my_bin)                                 # n=0 설정하여 while문으로 N번 만큼 돌며 16진수 각 자리수를 10진수로 변환하고 곧바로 4자리 2진수로 변환 
        my_result += my_bin                             # 이를 정답변수에 저장
        n += 1

    # print(my_result)

    # my_result += my_bin
    print("#{} {}".format(tc+1, my_result))
"""