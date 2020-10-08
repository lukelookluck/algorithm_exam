from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)  # deque에 prices list 넣기
    while dq:   # dq가 빌 때까지
        dq_popleft = dq.popleft()   # dq의 왼쪽에서 하나 꺼냄
        cnt = 0     # 기간 0으로 초기화
        for i in dq:    # dq를 돌면서 확인
            if dq_popleft > i:  # 바로 다음 기간에 가격이 떨어진다면
                cnt += 1    # 1초이므로 '기간(0) +1' 이 정답
                break
            cnt += 1    # 가격이 안 떨어진다면 '기간 +1' 하기
        answer.append(cnt)  # 가격이 떨어진 경우(break) or 포문 다 돈 경우, 정답 list에 cnt(기간)값 넣기

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))