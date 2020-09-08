
def powerset2(n):
    # n이 5일 경우, 리스트에 1, 2, 4, 8, 16(2^4)가 들어있음
    binary_digit_list = [1 << i for i in range(len(n))]

    for i in range(1 << len(n)):
        result = []
        for num, binary_digit in zip(n, binary_digit_list):
            if binary_digit & i:
                result.append(num)
        yield result


def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss, mask in zip(s, masks) if mask & i]


for power in powerset([1, 2, 3, 4, 5]):
    print(power)
