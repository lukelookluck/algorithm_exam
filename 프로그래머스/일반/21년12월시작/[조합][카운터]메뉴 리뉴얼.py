from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # course = 조합하는 개수들
    for c in course:
        temp = []
        for order in orders:
            for comb in combinations(order, c):
                # temp = 모든 주문의 음식들 조합
                temp.append(''.join(sorted(comb)))
        # 개별 개수
        counted_temp = Counter(temp).most_common()
        # 조합하는 개수별 최대 주문수의 주문 append
        for k, v in counted_temp:
            if v >= 2 and v == counted_temp[0][1]:
                answer.append(k)
           # 오름차순 정렬     
    return sorted(answer)
