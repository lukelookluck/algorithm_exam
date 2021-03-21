import sys


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
                n = lps[n - 1]
            else:
                i += 1
    return lps


def search(text, pat):
    i, j = 0, 0
    lps = to_lps(pat)
    cnt = 0

    while cnt < 720000:
        if text[i] == pat[j]:
            i += 1
            j += 1

            if j == 360000:
                return True

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if i == 360000:
            i = 0

        cnt += 1
    return False


N = int(sys.stdin.readline().strip())
pat, text = [0] * 360000, [0] * 360000
for x in map(int, sys.stdin.readline().split()):
    pat[x] = 1
for x in map(int, sys.stdin.readline().split()):
    text[x] = 1

if search(text, pat):
    print('possible')
else:
    print('impossible')
