total = 0
N = 10
A = [0 for _ in range(N)]
data = list(range(1, 11))

def print_set(n, sum):
    if sum == 10:
        for i in range(n):
            if A[i] == 1:
                print(data[i], end=' ')
        print()

def power_set(n, k, sum):
    global total

    if sum > 10:
        return
    total += 1
    if n == k:
        print_set(n, sum)

    else:
        A[k] = 1  # k번 요소 O
        power_set(n, k + 1, sum + data[k])  # 다음 요소 포함 여부 결정

        A[k] = 0  # k번 요소 X
        power_set(n, k + 1, sum)  # 다음 요소 포함 여부 결정


power_set(10, 0, 0)
print("호출회수 : {}".format(total))