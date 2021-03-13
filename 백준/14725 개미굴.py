import sys


class Node():
    def __init__(self, key):
        self.key = key
        self.child = {}


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, mystr):
        curr_node = self.head

        for s in mystr:
            if s not in curr_node.child:
                curr_node.child[s] = Node(s)
            curr_node = curr_node.child[s]

    def inquiry(self, cnt, curr_node):
        if cnt == 0:
            curr_node = self.head

        for c in sorted(curr_node.child.keys()):
            print('--' * cnt, c, sep='')
            self.inquiry(cnt+1, curr_node.child[c])


N = int(sys.stdin.readline().strip())
trie = Trie()
for _ in range(N):
    data = list(sys.stdin.readline().split())
    trie.insert(data[1:])

trie.inquiry(0, None)
