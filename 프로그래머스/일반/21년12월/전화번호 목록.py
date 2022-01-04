def solution(phone_book):
    phone_book = sorted(phone_book)
    hash = {}

    for phone_number in phone_book:
        hash[phone_number] = 1

    print(hash)
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in hash and temp != phone_number:
                return False

    return True

a = ["119", "97674223", "1195524421"]
print(solution(a))