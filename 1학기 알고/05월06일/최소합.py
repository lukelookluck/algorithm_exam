import sys
sys.stdin = open('최소합.txt')

def my_def(r, c, sum):
    global my_min
    # 오른쪽 아래에 도착하면, 그때까지의 sum과 my_min을 비교하여, sum이 my_min보다 작을 경우, my_min을 sum으로 바꿔주기
    if r == N-1 and c == N-1:
        if my_min > sum:
            my_min = sum
        return
    # 탐색 중, sum이 my_min보다 클 경우, 찾는 답이 아니므로 끝내버리기 a.k.a 가지치기
    elif my_min < sum:
        return
    # N-1 인덱스 내에서 행 + 1 그리고 열 + 1 하는 재귀 돌려주기
    else:
        if r+1 <= N-1:
            my_def(r+1, c, sum+arr[r+1][c])
        if c+1 <= N-1:
            my_def(r, c+1, sum+arr[r][c+1])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    # 최솟값 초기 설정
    my_min = float('inf')
    # 인덱스 (0, 0)부터 시작
    my_def(0, 0, arr[0][0])
    print("#{} {}".format(tc+1, my_min))

