def solution(answers):
    answer = []
    score = [0, 0, 0]
    rt_1 = [1, 2, 3, 4, 5]
    rt_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    rt_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == rt_1[i % len(rt_1)]:
            score[0] += 1
        if answers[i] == rt_2[i % len(rt_2)]:
            score[1] += 1
        if answers[i] == rt_3[i % len(rt_3)]:
            score[2] += 1

    print(score)

    my_max = max(score)
    for i in range(3):
        if my_max == score[i]:
            print(i)
            answer.append(i+1)
    print(answer)
    return answer


a = [1,3,2,4,2]

solution(a)