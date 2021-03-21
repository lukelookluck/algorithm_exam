def to_lps(pat, len_pat):
    lps = [0] * len_pat
    i, n = 1, 0

    while i < len_pat:
        if pat[i] == pat[n]:
            n += 1
            lps[i] = n
            i += 1
        else:
            if n != 0:
                n = lps[n-1]
            else:
                i += 1

    if not len_pat % (len_pat - lps[-1]):
        return len_pat // (len_pat - lps[-1])

    return 1


while True:
    pat = input()
    len_pat = len(pat)

    if pat == '.':
        break

    print(to_lps(pat, len_pat))