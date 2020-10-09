

def solution(boxes):
    answer = -1
    N = len(boxes)
    temp = []
    for i in boxes:
        temp += i
    b_len = len(temp)
    temp = set(temp)
    a_len = len(temp)
    answer = N - (b_len - a_len)

    return answer


boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
solution(boxes)