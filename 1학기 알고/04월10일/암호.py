import sys
sys.stdin = open('암호.txt')

# 이중 노드로 구현함
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0   # 출력시, 계산의 용이성을 위해 size 설정

    # 노드 맨 뒤에 추가
    def append(self, node):
        # 리스트가 존재 X
        if self.head is None:
            self.head = node
            self.tail = node

        # 리스트 존재 O
        else:
            self.tail.next = node   # 맨 뒤 노드의 다음 껄, 삽입할 노드로 설정
            node.prev = self.tail   # 삽입할 노드의 이전 껄, 리스트의 맨 뒤에 껄로 설정
            self.tail = node    # 노드를 삽입했으니, 삽입한 노드를 리스트의 맨 뒤에 껄로 설정
            self.head.prev = self.tail  # 원형 이중 리스트이므로, 리스트 머리를 꼬리와 연결
            self.tail.next = self.head  # 리스트 꼬리를 머리와 연결
        self.size += 1
        # mylist.print()



    # 디버깅용 단순 출력
    def print(self):
        current_node = self.head
        string = ""
        cnt = 0
        circuit = 0
        while current_node and circuit < 1:     # 처음엔 'and circuit < 1'를 입력 안 해서 출력함수 실행시, 무한루프에 걸렸었음..
            string += str(current_node.data) + " "
            current_node = current_node.next
            cnt += 1
            if cnt == self.size:
                circuit += 1
        print(string)

    # 문제의 풀이방식을 함수로 구현
    def formula(self, M, K):
        current_node = self.head
        cnt = 0
        while K > 0:    # K번 도니까 해당 조건 만족시 K -= 1 해서 K번 돌게 구현함

            if cnt == M:    # 조건 만족시
                previous_digit = current_node.prev.data     # 현재 전 노드의 값 저장
                next_digit = current_node.data      # 현재 노드의 값 저장
                new_node = Node(previous_digit+next_digit)      # 노드 생성 data = 현재 전 노드의 값+ 현재 노드의 값
                previous_node = current_node.prev       # 현재 전 노드 저장
                next_node = current_node        # 현재 노드 저장

                previous_node.next = new_node       # 현재 전 노드의 다음 링크를 신규 노드로
                new_node.prev = previous_node       # 신규 노드의 이전 링크를 현재 전 노드로

                next_node.prev = new_node       # 현재 노드의 이전 링크를 신규 노드로
                new_node.next = next_node       # 신규 노드의 다음 링크를 현재 노드로
                current_node = new_node     # 신규노드로 aim 바꾸기
                cnt = 0
                K -= 1
                self.size += 1

            cnt += 1
            current_node = current_node.next    # aim 노드 다음껄로 변경

    def result_print(self):
        current_node = self.head.prev       # aim 노드를 리스트 머리의 이전 노드로 하여 맨 뒤 설정
        # print(current_node.data)          # 그냥 리스트 꼬리 노드로 하니까 원하는 값이 출력 안되었음, 문제풀이 포뮬러 함수에서 따로 지정 안 해서 그럼
        cnt = 0                             # 포물러 함수에 self.tail = self.head.prev 로 했어야 함
        if self.size > 10:      # 리스트 사이즈 10 넘어가면 뒤에서 10개만 출력하라고 했으니
            while cnt < 10:
                result.append(current_node.data)
                current_node = current_node.prev
                cnt += 1
        else:
            while cnt < self.size:  # 리스트 10 이하시 뒤에서부터 출력
                result.append(current_node.data)
                current_node = current_node.prev
                cnt += 1






T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    arr = [*map(int, input().split())]

    mylist = DoubleLinkedList()
    result = []

    for i in arr:
        mylist.append(Node(i))

    # mylist.print()
    mylist.formula(M, K)
    # mylist.print()
    mylist.result_print()
    print("#{}".format(tc+1), *result)