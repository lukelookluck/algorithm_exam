import sys
sys.stdin = open('문제3.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    sum = sum2 = total = sum3 = 0
    total_sum = 0
    t = []
    l1 = []
    l2 = []
    l3 = []
    result = []

    # 전체 수확량
    for i in range(N):
        for j in range(N):
            total += arr[i][j]

    #젤 오른쪽 라인(+1)의 수확량을 l1에 추가(총 N개), 그리고 전체 수확량에서 그 값을 제외한 값을 t에 추가(총 N개)
    for j in range(N-1, 0, -1):
        for i in range(N):
            sum += arr[i][j]
        total_sum = total - sum
        l1.append(sum)
        t.append(total_sum)

    # l1 구역을 제외하고 젤 위쪽 라인(+1)의 수확량을 l2에 추가(총 N*N개)
    for j in range(N - 1, 0, -1):
        sum2 = 0
        for l in range(N-1):
            for k in range(0, j):
                sum2 += arr[l][k]
            l2.append(sum2)

    # 나머지 수확량은 t에서 l2를 빼서 l3에 추가(총 N*N개)
    for i in range(N-1):
        for k in range(N-1):
            l3.append(t[i] - l2[4*i+k])

    # 각 경우(l1 1개에 각 4개씩의 l2, l3의)의 최댓값과 최솟값을 구해 그 차이값의 최솟값 도출
    for i in range(N-1):
        for k in range(N-1):
            my_max = max(l1[i], l2[4*i+k], l3[4*i+k])
            my_min = min(l1[i], l2[4*i+k], l3[4*i+k])
            result.append(my_max - my_min)


    print("#{} {}".format(tc+1, result2))