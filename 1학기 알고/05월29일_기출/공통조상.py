import sys, time
sys.stdin = open('공통조상.txt')

st = time.time()


def my_func(x):
    global cnt
    # 부모노드의 자식노드 딕셔너리를 탐색하며 cnt += 1 해줌
    for i in my_list2[x]:
        cnt += 1
        if i in my_list2:
            my_func(i)


T = int(input())
for tc in range(T):
    V, E, FD1, FD2 = map(int, input().split())
    data = [*map(int, input().split())]
    # 트리를 딕셔너리로 저장하기 위한 딕셔너리 초기화
    my_list = {}
    my_list2 = {}

    # 계산의 용의성을 위해 딕셔너리를 2개로 나눔
    # my_list는 자손 노드에 대한 부모 노드 정보 딕셔너리
    # my_list2는 부모 노드에 대한 자식 노드 정보 딕셔너리
    for i in range(0, E*2, 2):
        if data[i+1] in my_list:
            my_list[data[i+1]] += data[i]
        else:
            my_list[data[i+1]] = data[i]
        if data[i] in my_list2:
            my_list2[data[i]] += [data[i+1]]
        else:
            my_list2[data[i]] = [data[i+1]]

    temp_list1, temp_list2 = [], []

    # 주어진 노드들의 부모노드 정보를 각각 temp_list1과 temp_list2에 저장
    while FD1:
        if FD1 in my_list or FD2 in my_list:
            if FD1 in my_list:
                temp_list1.append(my_list[FD1])
                FD1 = my_list[FD1]
            if FD2 in my_list:
                temp_list2.append(my_list[FD2])
                FD2 = my_list[FD2]
        else:
            break

    # 공통된 부모노드 정보를 저장하기 위한 리스트
    same_data = []
    for i in temp_list1[::-1]:
        if i in temp_list2:
            same_data.append(i)
        else:
            break
    print(same_data)

    # 공통조상의 모든 자식노드를 도출해야 하므로 자기 자신 1에서 시작
    cnt = 1
    my_func(same_data[-1])
    print("#{} {} {}".format(tc+1, same_data[-1], cnt))

print(time.time() - st)