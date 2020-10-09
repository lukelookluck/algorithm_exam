
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)     # str(숫자) 정렬기준 : 앞자리 기준으로 정렬됨
    return str(int(''.join(numbers)))


numbers = [6, 10, 2, 5, 6]
print(solution(numbers))