import sys
sys.stdin = open('수열 합치기.txt')


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:     # 이중 연결로 구현함
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node       # 꼬리 다음을 신규 노드로
            node.prev = self.tail       # 신규 노드 이전을 현재 리스트 꼬리로
            self.tail = node            # 리스트 꼬리를 신규 노드로

    def print(self):        # 디버깅용 리스트 값 단순 출력
        current_node = self.head
        string = ""
        while current_node:
            string += ' ' + str(current_node.data)
            current_node = current_node.next
        print(string)

    def insert_DataInfrontofData(self, list):       # 원하는 곳에 리스트를 넣는 함수
        current_node = self.head                    # 처음엔 리스트에 주어진 값들을 연결 리스트(ex: A)로 만들어 넣으면, 처음엔 원하는 대로 잘 작동하겠지만, 이후 A를 변경하면
        my_node = list.tail                         # 기존에 넣은 값들이 변경될 것이라 생각했는데, 그건 나의 착각이었음. 연결 리스트는 그냥 노드들을 묶어놓은 집단일 뿐, 기존의 '리스트'와는 다른 개념이었음

        while current_node:
            next_node = current_node                    # aim 노드를 현재노드(리스트 머리)로 설정, 이를 next노드로도 설정
            if current_node.data > temporary_list[0]:   # aim 노드의 값이 주어진 값들의 조건([0])보다 클 경우
                if current_node.prev:                   # 그 노드가 연결리스트의 맨 앞이 아닐 경우
                    previous_node = current_node.prev   # previous 노드를 현재 노드의 이전 노드로
                    previous_node.next = list.head      # previous 노드의 다음 링크를 주어진 값들로 만든 연결리스트(A)의 머리로
                    list.head.prev = previous_node      # A의 머리 이전 링크를 previous 노드로
                    list.tail.next = next_node          # A의 꼬리 다음 링크를 next 노드로
                    next_node.prev = my_node            # 현재 노드 이전 링크를 A의 꼬리로
                    return
                else:                           # 맨 앞일 경우
                    self.head = list.head       # 리스트 머리를 A 머리로
                    my_node.next = next_node    # A 꼬리 다음 링크를 현재 노드로
                    next_node.prev = my_node    # 현재 노드 이전 링크를 A 꼬리로
                    return
            current_node = current_node.next    # 현재 노드를 다음껄로 변경

        self.tail.next = list.head      # A를 리스트 맨 뒤로 넣어야 할 경우
        list.head.prev = self.tail
        self.tail = list.tail

    def result_print(self):
        global result

        cnt = 0
        current_node = self.tail
        while cnt < 10:         # 맨 뒤에서 10개 출력
            result.append(current_node.data)
            current_node = current_node.prev        # 현재 노드 이전 걸로 변경
            cnt += 1
        return


T = int(input())
for tc in range(T):
    N, M = map(int ,input().split())

    mylist = DoubleLinkedList()
    temporary_list2 = DoubleLinkedList()
    result = []
    temporary_list = [*map(int, input().split())]
    for i in temporary_list:
        mylist.append(Node(i))
    # mylist.print()

    for m in range(M-1):
        temporary_list = [*map(int, input().split())]
        for i in temporary_list:
            temporary_list2.append(Node(i))
        # print('0000000000000')
        # temporary_list2.print()
        mylist.insert_DataInfrontofData(temporary_list2)
        # mylist.print()
        temporary_list2.head = None
        temporary_list2.tail = None

    mylist.result_print()
    print("#{}".format(tc+1), *result)