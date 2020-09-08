import sys
sys.stdin = open('노드의 합.txt')


class BinaryTree:
    def __init__(self, N):
        self.node_list = [0] * (N + 1)          # 배열 생성 1에서 시작하므로 N+1 길이의 리스트 생성

    def inputValue(self, n1, n2):               # 해당 노드 번호에 값 반영
        self.node_list[n1] = n2

    def calculate(self, L):                     # 재귀로 합 구하는 함수 생성
        self.sum = 0
        self.calculating(L)
        return self.sum

    def calculating(self, digit):               # 계산 함수
        if digit * 2 > N:       # 조건에 해당하는 숫자는 자식 노드가 없는 것 따라서 해당 노드의 값을 합계에 합산  Ex) 1~9 노드번호 이진트리일 때, digit은 5인 조건
            self.sum += self.node_list[digit]
        else:                   # 그 외 조건일 경우
            if digit * 2 != N:      # ex) 1~9의 노드번호를 가진 이진트리일 경우, digit는 4의 값을 구하기 위해 노드번호 9에 접근하는 식
                self.calculating(digit * 2 + 1)

            self.calculating(digit * 2) # 위 경우의 노드번호 8에 접근하는 식


T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())

    my_tree = BinaryTree(N)             # 이진트리 생성
    for i in range(M):
        my_tree.inputValue(*map(int, input().split()))
    print("#{} {}".format(tc+1, my_tree.calculate(L)))