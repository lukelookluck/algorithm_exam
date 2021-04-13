import sys
sys.setrecursionlimit(10**6)


def divide(in_start, in_end, p_start, p_end):
    print(in_start, in_end, p_start, p_end)
    if(in_start > in_end) or (p_start > p_end):
        return

    parents = post_order[p_end]  # 부모노드 찾기
    print(parents, end=" ")

    left = pos[parents] - in_start  # 후위순회에서의 왼쪽인자 갯수
    right = in_end - pos[parents]  # 후위순회에서의 오른쪽인자 갯수
    print(left, right)
    divide(in_start, in_start + left - 1, p_start, p_start + left - 1)  # 왼쪽 노드
    print('asdasdasd')
    divide(in_end - right + 1, in_end, p_end - right, p_end - 1)  # 오른쪽 노드


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0] * (n+1)

for i in range(n):
    pos[in_order[i]] = i

divide(0, n-1, 0, n-1)