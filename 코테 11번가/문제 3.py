
def solution(A):
    len_A = len(A)
    correct_list = list(range(1, len_A+1))
    sorted_A = sorted(A)
    result = 0

    for i in range(len_A):
        if correct_list[i] != sorted_A[i]:
            result += abs(correct_list[i] - sorted_A[i])

    if result > 1000000000:
        return -1
    else:
        return result



T = 1
for tc in range(T):
    A = [6,2,3,5,6,3]

    print(solution(A))