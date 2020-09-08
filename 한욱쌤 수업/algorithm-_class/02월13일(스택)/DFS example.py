import sys
sys.stdin = open('DFS example.txt')

N = int(input())
data = list(map(int, input().split()))
arr = [[0 for _ in range(N)] for _ in range(N)]


for i in range(0, len(data), 2):
    arr[data[i]-1][data[i+1]-1] = 1
    arr[data[i+1]-1][data[i]-1] = 1


print(arr)

arr_visited = list(0 for _ in range(N))
print(arr_visited)

nabreak = True
I, J = 0, 0
for k in range(N):
    for i in range(I, N):
        for j in range(0, N):
            if arr[i][j] == 1:
                arr_visited[i] = 1
                I = j
                print(arr_visited)
                nabreak = False
                break
        if nabreak == False:
            break

