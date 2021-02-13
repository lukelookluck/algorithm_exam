import sys


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def _pre(node):
    print(node.value, end='')
    if node.left != '.':
        _pre(tree[node.left])
    if node.right != '.':
        _pre(tree[node.right])


def _in(node):
    if node.left != '.':
        _in(tree[node.left])
    print(node.value, end='')
    if node.right != '.':
        _in(tree[node.right])


def _post(node):
    if node.left != '.':
        _post(tree[node.left])
    if node.right != '.':
        _post(tree[node.right])
    print(node.value, end='')


N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    value, left, right = map(str, sys.stdin.readline().split())
    tree[value] = Node(value, left, right)

_pre(tree['A'])
print()
_in(tree['A'])
print()
_post(tree['A'])