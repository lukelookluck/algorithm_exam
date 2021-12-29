def solution(phone_book):
    phone_book = sorted(phone_book, key=len)

    for i in range(len(phone_book)):
        temp = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if temp == phone_book[j][:len(temp)]:
                return False

    return True

a = ["123","456","789"]
print(solution(a))