import sys
sys.stdin = open('서브트리.txt')


def my_func(p):
    global my_cnt
    my_cnt += 1                     # 본인 노드 +1
    if tree_dict.get(p):            # p 값에 해당되는 key의 value 리스트 소환
        for i in tree_dict.get(p):  # 1개 씩 빼서 재귀돌림
            my_func(i)
    else:
        return


T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    data = [*map(int, input().split())]
    verify_list = [*range(1, E+2)]      # 루트노드를 찾기 위한 리스트
    tree_dict = {}                      # 트리를 딕셔너리로 구현함
    my_cnt = 0                          # 개수 초기화
    for i in range(0, 2*E, 2):
        if data[i+1] in verify_list:        # 1 ~ E+1 의 숫자 중 자식노드에 해당되는 숫자 제거
            verify_list.remove(data[i+1])
        if data[i] not in tree_dict:        # 부모노드인데 딕셔너리에 없으면 key로 넣고 value값으로 해당 자식 노드를 넣음
            tree_dict[data[i]] = [data[i+1]]
        else:                               # 부모노드인데 이미 딕셔너리에 존재하면, 해당 자식 노드 값 value에 추가
            tree_dict[data[i]] += [data[i + 1]]

    if tree_dict:
        my_func(N)           # N 값의 하위 노드 구하기(본인 층 포함해서) ex: 2 - 3 - 4 순으로 계층이 이뤄져잇으면 개수 3
    print("#{} {}".format(tc+1, my_cnt))
