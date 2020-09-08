import sys
sys.stdin = open('그룹 나누기.txt')


# def make_set(x):
#     p[x] = x


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [*map(int, input().split())]
    p = [0] * (N+1)
    result = []

    """
    check_list = [0]*N
    result1 = 0

    for i in range(0, len(data), 2):
        if check_list[data[i+1]-1] != 1:
            check_list[data[i+1]-1] = 1
        elif check_list[data[i+1]-1] == 1:
            check_list[data[i]-1] = 1
        # print(check_list)
    result1 = 0
    for i in check_list:
        if i == 0:
            result1 += 1

    print("#{} {}".format(tc+1, result1))
    """

    for i in range(1, N+1):
        # 우선 p의 인덱스 1에서 N까지 자기 자신 넣기
        p[i] = i
        # make_set(i)

    for i in range(0, 2*M, 2):
        # 주어진 데이터를 통해 p의 data[i+1]번째에 data[i]값 넣기
        union(data[i], data[i+1])

    for i in p:
        # p에서 하나씩 뽑아 부모를 result에 삽입
        result.append(find_set(i))

    print("#{} {}".format(tc+1, len(set(result))-1))



