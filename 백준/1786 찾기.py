def to_lps(pat):
    lps = [0] * len(pat)

    i, n = 1, 0
    while i < len(pat):
        if pat[i] == pat[n]:
            n += 1
            lps[i] = n
            i += 1
        else:
            if n != 0:
                n = lps[n-1]
            else:
                i += 1
    return lps


def search(txt, pat, lps):
    T, P = len(txt), len(pat)
    i, j = 0, 0

    while i < T:
        if txt[i] == pat[j]:
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == P:
            answer.append(i - j + 1)
            j = lps[j-1]


txt = input()
pat = input()
answer = []

lps = to_lps(pat)

search(txt, pat, lps)
print(len(answer))
print(*answer)