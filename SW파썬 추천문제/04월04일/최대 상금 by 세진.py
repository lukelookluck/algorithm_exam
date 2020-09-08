import sys, time
sys.stdin = open('최대 상금.txt')


st = time.time()
T = int(input())
for test_case in range(1, 1 + T):
    number, cnt = input().split()
    number = list(map(int, number))
    cnt = int(cnt)
    N = len(number)

    result = 0
    stack = [(number, 0, 0)]
    while stack:
        number, idx, rep = stack.pop()
        if rep >= cnt:  # 종료
            sub_res = int(''.join(map(str, number)))
            if sub_res > result:
                result = sub_res
                continue

        if idx < N - 1:
            max_num = max(number[idx:])
            if number[idx] == max_num:
                stack.append((number, idx + 1, rep))
            else:  # number[idx]와 최대값들 중 하나와 바꿈
                for i in range(N - 1, idx, -1):
                    if number[i] == max_num:
                        sub_num = number[:]
                        sub_num[idx], sub_num[i] = sub_num[i], sub_num[idx]
                        stack.append((sub_num, idx + 1, rep + 1))

        else:  # cnt가 남을 때
            # 중복 숫자 찾기
            for i in range(N):
                if number[i] in number[i + 1:]:
                    break
            else:  # 중복 숫자 없음
                if (cnt - rep) % 2:  # 남은 횟수 홀수일 때
                    number[-1], number[-2] = number[-2], number[-1]

            # 종료
            sub_res = int(''.join(map(str, number)))
            if sub_res > result:
                result = sub_res

    print('#{} {}'.format(test_case, ''.join(map(str, number))))

print(time.time() - st)