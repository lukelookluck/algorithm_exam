from itertools import combinations

def solution(relation):
    answer = 0
    result = []
    row_N = len(relation)
    col_N = len(relation[0])
    com_range = list(range(col_N))
    for i in range(1, col_N + 1):
        c = combinations(com_range, i)
        result.extend(c)
    unique_list = []
    for i in result:
        temp =[]
        for j in range(row_N):
            temp2 = []
            for k in i:
                temp2.append(relation[j][k])
            temp.append(tuple(temp2))
        if len(set(temp)) == row_N:
            unique_list.append(i)
    final_list = set(unique_list)
    for i in range(0, len(unique_list)-1):
        for j in range(i+1, len(unique_list)):
            if set(unique_list[i]) == set(unique_list[i]) & set(unique_list[j]):
                final_list.discard(unique_list[j])
    print(len(final_list))



relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)
# solution2(relation)

