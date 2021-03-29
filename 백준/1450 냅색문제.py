from bisect import bisect_left


def a_brute_force(l, w):
    if l >= len(a_weight):
        a_sum.append(w)
        return

    a_brute_force(l + 1, w)
    a_brute_force(l + 1, w + a_weight[l])


def b_brute_force(l, w):
    if l >= len(b_weight):
        b_sum.append(w)
        return

    b_brute_force(l + 1, w)
    b_brute_force(l + 1, w + b_weight[l])


n, c = map(int, input().split())
weight = list(map(int, input().split()))
answer = 0

a_weight = weight[:n // 2]
b_weight = weight[n // 2:]

a_sum = []
b_sum = []

a_brute_force(0, 0)
b_brute_force(0, 0)

b_sum.sort()

for i in a_sum:
    if c - i < 0:
        continue
    answer += bisect_left(b_sum, c - i + 1)

print(answer)