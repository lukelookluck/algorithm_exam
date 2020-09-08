import sys
sys.stdin = open('단순 2진 암호코드.txt')

# 함수의 입력은 시작행, 시작열, 마지막 열
def my_func(si, sj, lj):
    tem_str = []
    tem_n, my_cnt, my_odd, my_even, my_result = 0, 1, 0, 0, 0
    for i in range(sj, lj+1):
        # 1칸씩 탐색하며, tem_str 리스트에 해당 값 append
        tem_n += 1
        tem_str.append(arr[si][i])
        # 7칸이 될 때마다, 암호 해석 딕셔너리에서 값을 꺼내와 tem_str과 비교 후 일치하면
        # 해당 키 값을 합산하되
        # 홀수번째(인덱스상 짝수)암호일 경우 my_odd에, 짝수번째(인덱스상 홀수)암호일 경우 my_even에 합산
        if tem_n == 7:
            for keys, values in my_keys.items():
                if values == tem_str:
                    if my_cnt % 2:
                        my_odd += int(keys)
                    else:
                        my_even += int(keys)
                    # 결과값 도출을 위해 각 칸의 키값을 my_result에 합산
                    my_result += int(keys)

            # tem_str, 탐색한 칸 개수 초기화, 암호 n+1번째로 만들어주기
            tem_str = []
            tem_n = 0
            my_cnt += 1

    # 암호가 검정된다면 my_result 출력
    if ((my_odd * 3) + my_even) % 10 == 0:
        print("#{} {}".format(tc + 1, my_result))

    # 잘못된 암호라면 0 출력
    else:
        print("#{} {}".format(tc + 1, 0))



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[*map(int, input())] for _ in range(N)]

    # 암호 해석을 위한 디셔너리 설정
    my_keys = {
        '0': [0, 0, 0, 1, 1, 0, 1],
        '1': [0, 0, 1, 1, 0, 0, 1],
        '2': [0, 0, 1, 0, 0, 1, 1],
        '3': [0, 1, 1, 1, 1, 0, 1],
        '4': [0, 1, 0, 0, 0, 1, 1],
        '5': [0, 1, 1, 0, 0, 0, 1],
        '6': [0, 1, 0, 1, 1, 1, 1],
        '7': [0, 1, 1, 1, 0, 1, 1],
        '8': [0, 1, 1, 0, 1, 1, 1],
        '9': [0, 0, 0, 1, 0, 1, 1],
    }

    # 주어진 배열에서 맨 뒤 열부터 탐색하여 1을 찾을 경우, 해당 인덱스값을 함수에 넘기고 tc를 종료
    my_bool = False
    for i in range(N):
        if my_bool is True:
            break
        for j in range(M-1, M-56+1, -1):
            if arr[i][j] == 1:
                my_bool = True
                # 행은 i, 열은 암호가 총 56자리므로 탐색한 j인덱스에서 56-1(인덱스는 0부터 시작하므로)를 뺀 값, 그리고 j를 넘겨줌
                my_func(i, j-(56-1), j)
                break