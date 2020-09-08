from collections import deque
import sys
sys.stdin = open('문자열 압착.txt')

def my_func(word):
    n = len(word)
    answer = len(word)
    for i in range(1, n//2 + 1):
        my_word = ''
        cnt = 1
        comfirm_word = word[0:i]
        print(i)
        for j in range(i, n+i, i):
            compare_word = word[j:j+i]
            print('comfirm_word', comfirm_word, j)
            print('compare_word', compare_word, j+i)
            print(my_word)

            # if len(comfirm_word) > len(compare_word):
                # print('기준글자가 더 길어')
                # if cnt > 1:
                #     my_word += str(cnt)
                # my_word += comfirm_word
                #
                # print(my_word)

            if comfirm_word == compare_word:
                cnt += 1
            elif comfirm_word != compare_word or len(comfirm_word) > len(compare_word):
                if cnt > 1:
                    my_word += str(cnt) + comfirm_word
                else:
                    my_word += comfirm_word
                comfirm_word = compare_word
                cnt = 1
            comfirm_word = word[j:j+i]
        answer = min(len(my_word), answer)
        print(my_word)







T = int(input())
for tc in range(T):
    word = input()
    my_func(word)
    print('---')
