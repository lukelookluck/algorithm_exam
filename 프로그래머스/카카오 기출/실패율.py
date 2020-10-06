
def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        print(i)
        cnt = stages.count(i)
        print(cnt, length, cnt/length)
        if length:
            answer.append([i, cnt/length])
        else:
            answer.append([i, 0])
        length -= cnt
    answer = sorted(answer, key=lambda x: (x[1]), reverse=True)
    print(list(map(lambda x: x[0], answer)))





N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)