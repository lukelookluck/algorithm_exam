import time
start = time.time()


def printarr(n):
    global cnt
    print(arr)
    cnt += 1
    return

def perm(n, k):
    if k == n:
        printarr(n)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [0] * 4
cnt = 0
perm(4, 0)
print(time.time() - start)
print(cnt)