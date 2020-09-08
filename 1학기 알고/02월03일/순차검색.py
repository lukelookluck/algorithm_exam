def sequentialSearch(a, n, key):
    i = 0 # i에 0을 할당
    while i < n and a[i] != key:
        i = i+1
    if i < n:
        return i
    else:
        return -1


def sequentialSearch2(a, n, key):
    i = 0 # i에 0을 할당
    i = i + 1
    while i < n and a[i] < key:
        i = i + 1
    if i < n and a[i] == key:
        return i
    else:
        return -1