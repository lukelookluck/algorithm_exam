import sys
sys.stdin = open('길찾기.txt')

def my_func(root):
    global answer

    if root == 99:
        answer = 1
        return

    else:
        if root in visited:
            return
        else:
            visited.append(root)
            if root in my_list:
                for i in my_list[root]:
                    my_func(i)

T = 10
for tc in range(T):
    a, len = map(int, input().split())
    data = list(map(int, input().split()))
    my_list = {}
    visited = []
    answer = 0

    for i in range(0, len*2, 2):
        if data[i] in my_list:
            my_list[data[i]] += [data[i+1]]
        else:
            my_list[data[i]] = [data[i+1]]

    my_func(0)
    print("#{} {}".format(tc+1, answer))

