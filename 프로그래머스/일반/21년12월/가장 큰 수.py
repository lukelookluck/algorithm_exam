def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) # 원소는 0 이상, 1000 이하이므로 * 3을 해줌

    return str(int(''.join(numbers)))
