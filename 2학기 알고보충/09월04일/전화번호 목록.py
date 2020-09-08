def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    present_word = ''

    n = len(phone_book)
    for i in range(n):
        present_word = phone_book[i]
        present_n = len(present_word)
        for j in range(i+1, n):
            if present_word == phone_book[j][:present_n]:
                answer = False
                break
        if answer is False:
            break



    return answer