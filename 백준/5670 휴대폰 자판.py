import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.cnt = 0
        # self.end = False


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
        # curr_node.end = True

    def inquiry(self, cnt, curr_node):
        global answer
        print('answer', answer)
        print(curr_node.key, curr_node.cnt, curr_node.end)
        print(curr_node.child.keys())

        if curr_node.cnt > 1:
            cnt += 1
        if curr_node.end:
            answer += cnt
            print('??', answer)
        for s in curr_node.child.keys():
            print(curr_node.child[s].cnt)
            self.inquiry(cnt, curr_node.child[s])

try:
    while True:
        N = int(sys.stdin.readline())
        trie = Trie()
        for _ in range(N):
            mystr = sys.stdin.readline().strip()
            trie.insert(mystr)
        answer = 0
        trie.inquiry(0, trie.head)
        print(answer)
        print(format(round(answer / N, 2), '.2f'))

except:
    exit(0)