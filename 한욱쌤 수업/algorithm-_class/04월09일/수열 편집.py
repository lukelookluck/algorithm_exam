import sys
sys.stdin = open('수열 편집.txt')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # 인덱스 추가
    def insertDataInfrontofIndex(self, idx, node):
        current_node = self.head
        current_i = 0
        previous_node = None

        if idx == 0:
            if self.head:
                next_node = self.head
                self.head = node
                self.head.next = next_node
            else:
                self.head = node
        else:
            while current_i < idx:
                if current_node:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    break
                current_i += 1

            if current_i == idx:
                node.next = current_node
                previous_node.next = node
            else:
                return -1

    # 인덱스 삭제
    def delete(self, idx):
        current_node = self.head
        previous_node = None
        current_i = 0
        if idx == 0:
            self.head = current_node.next
        else:
            while current_i < idx:
                if current_node:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    break
                current_i += 1

            if current_i == idx:
                previous_node.next = current_node.next
            else:
                return -1

    # 해당 인덱스 값 변경
    def editAtIndex(self, idx, value):
        current_node = self.head
        current_i = 0
        while current_i < idx:
            if current_node:
                current_node = current_node.next
            else:
                break
            current_i += 1
        if current_i == idx:
            current_node.data = value
        else:
            return -1

    # 출력
    def print(self):
        current_node = self.head
        string = ""
        while current_node:
            string += str(current_node.data)
            current_node = current_node.next
        print(string)

    # 원하는 인덱스의 값 출력
    def getIndexData(self, idx):
        current_node = self.head
        current_i = 0
        if idx == 0:
            if current_node:
                return current_node.data
            else:
                return -1
        else:
            while current_i < idx:
                if current_node:
                    current_node = current_node.next
                else:
                    break
                current_i += 1
            if current_i == idx:
                return current_node.data
            else:
                return -1

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    data = [*map(int, input().split())]

    mylist = SingleLinkedList()

    for i in data:
        mylist.append(Node(i))

    for m in range(M):
        add_list = [*map(str, input().split())]
        if add_list[0] == 'I':
            mylist.insertDataInfrontofIndex(int(add_list[1]), Node(int(add_list[2])))
        if add_list[0] == 'D':
            mylist.delete(int(add_list[1]))
        if add_list[0] == 'C':
            mylist.editAtIndex(int(add_list[1]), int(add_list[2]))

    print("#{} {}".format(tc+1, mylist.getIndexData(L)))