from collections import Counter
import sys

N = int(sys.stdin.readline().strip())
N_data = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_data = list(map(int, sys.stdin.readline().split()))

result = Counter(N_data)

for m in M_data:
    print(result[m], end=' ')