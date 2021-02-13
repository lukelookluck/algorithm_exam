
def solution(s):
    answer = 0
    s_len = len(s)

    for i in range(s_len):
        for j in range(i, s_len):
            word = s[i:j+1]
            w_len = len(word)
            idx = 0
            my_max = 0
            while idx != w_len - 1:
                if my_max > w_len - idx - 1:
                    break

                for r in range(w_len, idx, -1):
                    if word[idx] != word[r-1] and my_max < r - idx - 1:
                        my_max = r - idx - 1

                idx += 1
            answer += my_max

    return answer


s = "baby"
print(solution(s))