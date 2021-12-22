from collections import defaultdict


def solution(n, results):
    answer = 0
    win_g = defaultdict(set)
    lose_g = defaultdict(set)

    for w, l in results:
        win_g[l].add(w)
        lose_g[w].add(l)

    for i in range(1, n+1):
        for win in win_g[i]:
            lose_g[win].update(lose_g[i])
        for lose in lose_g[i]:
            win_g[lose].update(win_g[i])

    for i in range(1, n+1):
        if len(win_g[i]) + len(lose_g[i]) == n-1:
            answer += 1

    return answer