from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for i in range(len(progresses)):
        left_progress = 100 - progresses[i]
        dq.append(math.ceil(left_progress / speeds[i]))     # 각 기능의 남은 진도를 진도 속도로 나눈 값의 올림한 값(진도 100%까지 남은 기간(이하 남은 기간))을 dq에 저장

    n = 0                               # 보고있는 인덱스(n) 0으로 초기화
    length = len(dq)                    # 기능들의 총 개수 length 저장
    while dq:

        if n == length:                 # n == length 일 경우, 전체 기능을 다 본 것이므로 while 종료
            break
        ps_dq = dq[n]                   # ps_dq = 현재 보고있는 기능
        cnt = 1                         # 현재 기능 포함해야하므로 cnt = 1

        for i in range(n+1, length):    # n 다음 것부터 탐색하므로 n+1
            if ps_dq < dq[i]:           # 탐색 중, 남은 기간이 n보다 큰 값일 경우, for 문 종료
                break
            else:                       # 탐색 중, 남은 기간이 n보다 작은 값일 경우, cnt += 1, n += 1 (여기서 n += 1 한 값은 현재 보고 있는 기능에 영향 x)
                cnt += 1
                n += 1

        answer.append(cnt)              # for 문 종료 후, cnt 값 answer 저장
        n += 1



    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))