import sys
sys.stdin = open('작업순서.txt')

def my_func(k):
    visit[k] = 1

    for m in range(V):
        if arr[m][k] == 1 and visit[m] != 1:
            my_func(m)
    print(k+1, end= ' ')

T = 10
for tc in range(T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[0] * V for _ in range(V)]
    visit = [0] * V
    for i in range(0, len(data), 2):
        arr[data[i]-1][data[i+1]-1] = 1

    print("#{}".format(tc+1), end=' ')
    for i in range(V):
        count = 0
        for j in range(V):
            if arr[i][j] == 1:
                count += 1
                break
        if count == 0:
            my_func(i)
    print()