import sys, time
sys.stdin = open('장훈이의 높은 선반.txt')

st = time.time()

def my_func(N, s, sum):
    global my_sum
    # 문제의 조건이 B보다 클 때 이므로
    if sum >= B:
        # 기존의 최소값보다 작을 경우, 값 교체
        if my_sum > sum:
            my_sum = sum
            # 내 생각엔, 값 교체 후 계속 재귀를 돌려봤자 현재값은 늘어나므로 리턴으로
            # 종료해주는 게 낫다고 생각하는데, 시간은 return 없는게 더 빠름;;
            return
        # 기존의 최소값보다 클 경우, 리턴
        else:
            return
    # s가 N 끝까지 다 돌았을 경우, 리턴(N_spec에서 인덱스 에러 안 나게)
    if N == s:
        return
    else:
        # 부분집합 알고리즘과 비슷
        my_func(N, s+1, sum + N_spec[s])
        my_func(N, s+1, sum)



T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    N_spec = list(map(int, input().split()))
    # 최소값 찾기 위한 초기 최대값 설정
    my_sum = float('inf')
    my_func(N, 0, 0)
    print("#{} {}".format(tc+1, my_sum - B))
print(time.time() - st)