import sys
sys.stdin = open('가사 검색.txt')


class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.len = []


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.len_list = {}

    def insert(self, word, reverse):
        current_node = self.head

        if reverse:
            word = word[::-1]

        self.len_list[word] = len(word)

        for w in word:
            if w not in current_node.child:
                current_node.child[w] = Node(w)
            current_node.len.append(len(word))

            current_node = current_node.child[w]

    def search(self, query, reverse):
        current_node = self.head
        len_query = len(query)
        n = 0

        if reverse:
            if query[::-1] in used:
                return used[query[::-1]]

        for q in query:
            if q not in current_node.child:
                if q == '?':
                    a = current_node.len.count(len_query)
                    if query not in used:
                        if reverse:
                            query = query[::-1]
                        used[query] = a
                    return a
                else:
                    if query not in used:
                        if reverse:
                            query = query[::-1]
                        used[query] = 0
                    return 0

            current_node = current_node.child[q]


T = int(input())
for tc in range(T):
    words = list(map(str, input().split()))
    queries = list(map(str, input().split()))
    used = {}
    answer = []

    trie = Trie()
    r_trie = Trie()

    for word in words:
        trie.insert(word, False)
        r_trie.insert(word, True)

    for query in queries:
        print(used)
        # if query in used:
        #     answer.append(used[query])
        #     break
        if query[0] == '?':
            answer.append(r_trie.search(query[::-1], True))
        else:
            answer.append(trie.search(query, False))
        # print(used)
    print(answer)