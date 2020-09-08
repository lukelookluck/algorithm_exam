import sys
sys.stdin = open('숫자 추가.txt')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        # 리스트가 존재하지 않는다면
        if self.head is None:
            self.head = self.tail = node
        # 리스트 존재할 경우
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def inserAtIndex(self, idx, node):
        current_node = self.head
        current_i = 0
        previous_node = None

        # 맨 앞에 삽입
        if idx == 0:
            # head가 있으면 리스트가 존재한다는 말
            if self.head:
                next_node = self.head
                self.head = node
                self.head.next = next_node
            # 리스트 존재하지 않음
            else:
                self.head = node
            self.size += 1
        # 그 외에 삽입
        else:
            # 삽입하려는 인덱스 바로 앞의 정보를 알아야 함
            while current_i < idx:
                if current_node:
                    previous_node = current_node
                    current_node = current_node.next
                # 현재 노드가 없음, 즉 리스트의 맨 뒤일 경우
                else:
                    break
                current_i += 1
            # 원하는 인덱스일 경우
            if current_i == idx:
                node.next = current_node
                previous_node.next = node
            # 원하는 인덱스가 구라일 때
            else:
                return -1
            self.size += 1

    def print(self):
        # 현재노드는 리스트의 대가리
        current_node = self.head
        string = ""
        # 현재노드가 없어질 때까지
        while current_node:
            string += str(current_node.data)
            # 현재노드는 한 칸 뒤에껄로 해주기
            current_node = current_node.next
        print(string)

    def getIndexData(self, idx):
        # 현재노드는 리스트의 대가리
        current_node = self.head
        current_i = 0
        # 리스트 내의 노드 다 살피기
        while current_node:
            # 현재 인덱스가 원하는 인덱스일 경우
            if current_i == idx:
                # 그 노드의 데이터 리턴~
                return current_node.data
            current_node = current_node.next
            current_i += 1
        return -1

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    data = [*map(int, input().split())]

    my_linked_list = SingleLinkedList()
    for i in data:
        my_linked_list.append(Node(i))

    # 주어진 인덱스, 데이터를 (연결) 리스트에 넣기
    for m in range(M):
        my_idx, my_data = map(int, input().split())
        my_linked_list.inserAtIndex(my_idx, Node(my_data))

    print("#{} {}".format(tc+1, my_linked_list.getIndexData(L)))

