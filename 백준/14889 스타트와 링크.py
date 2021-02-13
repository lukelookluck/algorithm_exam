import sys
from itertools import combinations

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

my_comb = list(combinations(list(range(N)), N//2))
my_min = float('inf')

for i in range(len(my_comb) // 2):
    teamA = 0
    for a in my_comb[i]:
        for aa in my_comb[i]:
            teamA += data[a][aa]
    teamB = 0
    for b in my_comb[-i - 1]:
        for bb in my_comb[-i - 1]:
            teamB += data[b][bb]

    if abs(teamA - teamB) < my_min:
        my_min = abs(teamA - teamB)

print(my_min)