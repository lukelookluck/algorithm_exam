# data = [2, 4, 7, 10]
# 하나씩 뽑아서 곱한 걸 a에 추가
# 곱한 수의 자릿수가 data의 요소보다 클 경우, result에 추가
# result 요소 값 중에 가장 큰 값 출력

import sys
sys.stdin = open("정곤이의 단조 증가하는 수.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    result = []




    for i in range(len(data)):
        for j in range(i+1, len(data)):
            strn = str(data[i] * data[j])

            for k in range(len(strn)-1):
                if(strn[k] > strn[k+1]):
                    break
            else:
                result.append(int(strn))



    mmax = -1
    if(result):
        for i in result:
            if(i > mmax):
                mmax = i




    print("#{} {}".format(tc+1, mmax))
