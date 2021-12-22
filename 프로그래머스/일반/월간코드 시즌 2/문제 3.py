result = 0

def solution(a, edges):
    global result
    answer = float('inf')
    dist = {i: [] for i in range(len(a) + 1)}

    # print(check)
    for edge in edges:
        dist[edge[0]].append(edge[1])
        dist[edge[1]].append(edge[0])

    # print(dist)
    check = [-1] * (len(a) + 1)
    check[0] = 1

    if not search(a, check, dist, 0):
        answer = min(answer, result)
    else:
        answer = -1
    print(answer)
    return answer



def search(a, check, dist, digit):
    global result

    temp = a[digit]
    print('temp', temp)
    for x in dist[digit]:
        if check[x] == -1:
            print('x', x)
            check[x] = 1
            print('a[x]', a[x])
            temp += search(a, check, dist, x)
            print('temp', temp)
    result += temp
    return temp




a = [-5, 0, 2, 1, 2]
edges = [[0,1],[3,4],[2,3],[0,3]]
solution(a, edges)
