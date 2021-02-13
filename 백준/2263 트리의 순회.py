import sys

n = int(sys.stdin.readline())
in_arr = list(map(int, sys.stdin.readline().split()))
post_arr = list(map(int, sys.stdin.readline().split()))

class Node:
    def __init__(self, value, left, right):
        self.value = value
        if left == value:
            self.left = None
        else:
            self.left = left
        if right == value:
            self.right = None
        else:
            self.right = right

def solution(in_arr, post_arr, idx):
    if len(in_arr) <= 0 or len(post_arr) <= 0:
        # tree[idx] = Node(idx, None, None)
        return

    in_idx = in_arr.index(idx)
    post_idx = post_arr.index(idx)
    # print(in_arr, post_arr)
    # print(in_idx, post_idx)
    if post_arr[in_idx-1] != post_arr[post_idx-1]:
        tree[idx] = Node(idx, post_arr[in_idx-1], post_arr[post_idx-1])
    else:
        tree[idx] = Node(idx, post_arr[in_idx - 1], None)
    # print(in_arr[:in_idx], post_arr[:in_idx], post_arr[in_idx-1])
    # print(in_arr[in_idx+1:], post_arr[in_idx:post_idx], post_arr[post_idx-1])
    # print(tree)
    solution(in_arr[:in_idx], post_arr[:in_idx], post_arr[in_idx-1])
    solution(in_arr[in_idx+1:], post_arr[in_idx:post_idx], post_arr[post_idx-1])


def _pre(node):
    print(node.value, end=' ')
    if node.left != None:
        _pre(tree[node.left])
    if node.right != None:
        _pre(tree[node.right])

tree = {}
# n = 11
# in_arr = [7,4,8,2,5,1,9,6,11,10,3]
# post_arr = [7,8,4,5,2,9,11,10,6,3,1]
solution(in_arr, post_arr, post_arr[-1])
# print(tree[2].right)
_pre(tree[post_arr[-1]])