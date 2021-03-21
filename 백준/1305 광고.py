def to_lps(pat, L):
    lps = [0] * L
    i, n = 1, 0

    while i < L:
        if pat[i] == pat[n]:
            n += 1
            lps[i] = n
            i += 1
        else:
            if n != 0:
                n = lps[n-1]
            else:
                i += 1

    return lps[-1]


L = int(input())
pat = input()
a = to_lps(pat, L)
print(L - a)