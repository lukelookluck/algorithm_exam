from itertools import permutations

def solution(numbers):
    answer = 0
    my_set = set()
    for i in range(1, len(numbers) + 1):
        for x in list(map(''.join, permutations(numbers, i))):
            my_set.add(int(x))

    print(my_set)

    for ms in my_set:
        my_bool = True
        if int(ms) >= 2:
            for i in range(2, (int(ms) // 2)):
                if int(ms) % i == 0:
                    my_bool = False
            if my_bool:
                answer += 1

    return answer


n = "011"
solution(n)