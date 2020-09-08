import sys
sys.stdin = open('전자카트.txt')

# 문제가 설명을 이상하게 해놔서 많이 해맸음
# 만약 N=3일 경우, 1 2 3, 1 3 2 가능
# N=4일 경우, 1 2 3 4, 1 2 4 3, 1 3 2 4, 1 3 4 2, 1 4 3 2, 1 4 2 3 가능
# 즉, 맨 앞의 수는 놔두고 남은 N-2개의 순열을 구하면 됨

def permutation(r):
    global my_min
    # chosen의 길이가 N이 될 경우, 결과값 도출
    # 만약 N=3인 1 2 3 이 나올 경우. my_sum = data[1][2] + data[2][3] + data[3][1]
    if len(chosen) == r:
        my_sum = 0
        for i in range(N):  # N=3일 경우, i는 0 1 2, i가 2일 때, data[2][0] 해주기
            if i == N-1:
                my_sum += data[chosen[i]][chosen[0]]
            else:
                my_sum += data[chosen[i]][chosen[i+1]]
            # my_sum값 구하는 도중, my_min보다 클 경우, 걍 끝내기
            if my_sum >= my_min:
                return
        # 도출한 my_sum이 my_min보다 작을 경우, my_min으로 설정
        if my_sum < my_min:
            my_min = my_sum
        return

    # 맨 앞 0을 제외하고 1부터 N-1까지 돌면서 2부터 N-1까지 숫자 중 사용하지 않은 것을 차례대로 chosen 리스트에 투입
    for i in range(1, N):
        if used[i] != 1:
            chosen.append(arr[i])
            used[i] = 1
            permutation(r)
            # 이후 해당 자리의 숫자를 빼주어 재귀가 돌 수 있게 해줌
            used[i] = 0
            chosen.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    # 주어진 배열은 data로 저장
    data = [[*map(int, input().split())] for _ in range(N)]
    # 0부터 N까지 리스트 생성
    arr = [*range(N)]
    # 순열을 만들기 위해 사용할 used 리스트 생성
    used = [0 for _ in range(N)]
    # 최저값 초기설정
    my_min = float('inf')
    # 도출할 리스트의 맨 앞은 0이므로
    chosen = [0]
    # 재귀함수 실행
    permutation(N)
    print("#{} {}".format(tc+1 ,my_min))