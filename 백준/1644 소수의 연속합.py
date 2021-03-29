import sys


def check(digit):
    data = [True] * (digit + 1)

    for i in range(2, int(digit ** 0.5) + 1):
        if data[i]:
            data[2 * i::i] = [False] * ((digit - i) // i)

    return [i for i in range(2, digit + 1) if data[i]]


N = int(sys.stdin.readline().strip())
prime_number = check(N)
prime_number.append(0)
start, end = 0, 1
my_sum = prime_number[0]
answer = 0

while start < end < len(prime_number):
    if my_sum == N:
        answer += 1

    if my_sum >= N:
        my_sum -= prime_number[start]
        start += 1
    else:
        my_sum += prime_number[end]
        end += 1

print(answer)