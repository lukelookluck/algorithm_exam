import sys, time
sys.stdin = open('이진탐색.txt')
# start = time.time()

def my_binary_search_func(digit, fd, ld, my_bool):   # 인자: 찾는 숫자, 시작 인덱스, 끝 인덱스, 양쪽구간 검증 변수(왼쪽일 경우 1, 오른쪽일 경우 2)
    global cnt
    # m 초기화
    m = (fd + ld) // 2
    # 찾는 숫자가 인덱스 m 이라면 cnt += 1 해주기
    if digit == list_A[m]:
        cnt += 1
    # 찾는 숫자가 리스트 A의 중간 값보다 작을 경우
    elif digit < list_A[m]:
        # 만약 검증 변수가 1이라면, 조건에 해당되지 않으므로 끝내기
        # 현 구간이 리스트의 왼쪽 구간인데 다음 함수에서 또 왼쪽구간을 탐색해야한다면
        if my_bool == 1:
            return
        # 검증 변수를 1로, 끝 인덱스를 m-1로 하여 다시 함수 돌리기
        my_binary_search_func(digit, fd, m-1, 1)
    # 찾는 숫자가 리스트 A의 중간 값보다 클 경우
    else:
        # 만약 검증 변수가 2이라면, 조건에 해당되지 않으므로 끝내기
        if my_bool == 2:
            return
        # 검증 변수를 2로, 시작 인덱스를 m+1로 하여 다시 함수 돌리기
        my_binary_search_func(digit, m+1, ld, 2)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    list_A = [*map(int, input().split())]
    list_B = [*map(int, input().split())]
    # 리스트 A 정렬하기
    list_A.sort()
    # 결과값 cnt 초기화
    cnt = 0
    for i in list_B:
        # 리스트 B에서 하나씩 꺼내어 함수 돌리기
        # 하나씩 꺼낸 숫자가 리스트 A에 있다면 함수 돌리려고 했는데, 이 방식은 시간이 너무 걸려서 없애버림
        # if i in list_A:
        my_binary_search_func(i, 0, len(list_A)-1, 0)
    print("#{} {}".format(tc+1, cnt))

# print("WorkingTime: {} sec".format(time.time() - start))
