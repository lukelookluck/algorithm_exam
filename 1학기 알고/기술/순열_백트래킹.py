import time
start = time.time()


def perm(n, k):
    if n == k:
        print(t)
        # pass
    else:
        for i in range(n):
            if visited[i]:
                continue
            t[k] = a[i]
            print(t)
            visited[i] = True
            perm(n, k+1)
            visited[i] = False


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [0] * 3
visited = [0] * 10
for i in range(1, 4):
    perm(i, 0)
# print(time.time() - start)