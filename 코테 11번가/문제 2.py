

def solution(S):
    len_S = len(S)
    len_M = len(S[0])
    result = []
    for i in range(len_S - 1):
        for j in range(i+1, len_S):
            for k in range(len_M):
                if S[i][k] == S[j][k]:
                    return [i, j, k]

    return result






T = 1
for tc in range(T):
    # S = ['zzzz', 'ferz', 'zdsr', 'fgtd']
    # S = ['gr', 'sd', 'rg']
    S = ['bzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzz', 'bzdsrdazdsrdafgzzferzzzbzdsrdafgzzferzzzfgzzferzzzbzdsrdafgzzferzzzbbzdsrdafgzzferzzzbzdsrdafgzzferzzzbzdsrdafgzzferzzz']

    print(solution(S))