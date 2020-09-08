def bruteforce(text, patten):
    i, j = 0, 0
    len_text = len(text)
    len_patten = len(patten)
    while j < len_text and i < len_patten:
        if text[j] != patten[i]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == len_patten:
        return j - len_patten
    else:
        return -1

text = "ttttaacca"
patten = "cca"

print("{}".format(bruteforce(text, patten)))