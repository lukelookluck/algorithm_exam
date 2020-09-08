import sys, time
sys.stdin = open('최소 생산 비용.txt')
start = time.time()


def my_permutation(n, k, my_sum2):
    global result
    # 하나의 순열을 완성해가는 도중, 그 미완성의 순열을 적용한 비용이 기존의 최소비용(result-최소비용을 찾기위한 비교값)보다 클 경우, return
    if my_sum2 > result:
        return
    # 하나의 순열을 완성한 경우, 그 순열을 적용한 비용이 비교값(result)보다 작을 경우, 이를 최소값(result)으로 설정
    if k == n:
        if result > my_sum2:
            result = my_sum2
    # 순열 만드는 코드
    else:
        for i in range(k, n):
            my_list[k], my_list[i] = my_list[i], my_list[k]
            # 순열을 인덱스 k(0)에서 n까지 만들되, 3번째 인자에 순열의 k번째 인덱스에 해당하는 비용값을 더 해줌(가지치기를 위해서)
            my_permutation(n, k+1, my_sum2 + arr[k][my_list[k]])
            my_list[k], my_list[i] = my_list[i], my_list[k]


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    # 순열 만들기 위한 [0 ~ N-1]의 리스트 생성
    my_list = [*range(N)]
    # 최소 비용 찾기위한 비교값 생성
    result = float('inf')
    my_permutation(N, 0, 0)
    print("#{} {}".format(tc+1, result))
print(time.time() - start)