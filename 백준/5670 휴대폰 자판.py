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
        cn = self.head

        for s in mystr:
            if s not in cn.child:
                cn.child[s] = Node(s)
            cn = cn.child[s]
            cn.cnt += 1
        cn.child[' '] = False

    def inquiry(self, cnt, cn):
        global answer

        for s in cn.child.keys():
            if s != ' ':
                if len(cn.child) > 1 or cnt == 0:
                    answer += cn.child[s].cnt
                self.inquiry(cnt+1, cn.child[s])


try:
    while True:
        N = int(sys.stdin.readline())
        trie = Trie()
        for _ in range(N):
            trie.insert(sys.stdin.readline().strip())
        answer = 0
        trie.inquiry(0, trie.head)
        print(format(round(answer / N, 2), '.2f'))

except:
    exit(0)