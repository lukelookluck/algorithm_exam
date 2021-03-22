import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.cnt = 0


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, mystr):
        curr_node = self.head

        for s in mystr:
            if s not in curr_node.child:
                curr_node.child[s] = Node(s)
                curr_node.cnt += 1
            curr_node = curr_node.child[s]

    def inquiry(self, cnt, curr_node):
        global answer

        # print(curr_node.key, curr_node.cnt)
        if cnt == 0 and curr_node.cnt == 1:
            cnt += 1

        if curr_node.cnt == 0:
            answer += cnt

        if curr_node.cnt == 1:
            for s in curr_node.child.values():
                self.inquiry(cnt, s)
        else:
            for i, t in curr_node.child.items():
                if i == ' ':
                    self.inquiry(cnt, t)
                else:
                    self.inquiry(cnt+1, t)

try:
    while True:
        N = int(sys.stdin.readline())
        trie = Trie()
        for _ in range(N):
            mystr = sys.stdin.readline().strip() + ' '
            trie.insert(mystr)
        answer = 0
        trie.inquiry(0, trie.head)
        print(format(round(answer / N, 2), '.2f'))

except:
    exit(0)