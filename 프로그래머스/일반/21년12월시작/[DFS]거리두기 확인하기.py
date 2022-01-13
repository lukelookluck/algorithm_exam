def solution(places):
    answer = []
    xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def first(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    check = [[0] * 5 for _ in range(5)]
                    if not search(place, check, i, j, 0):
                        answer.append(0)
                        return
        answer.append(1)

    def search(place, check, a, b, cnt):
        check[a][b] = 1
        if cnt >= 2:
            return True
        for temp in xy:
            x, y = temp[0], temp[1]
            new_a = a + x
            new_b = b + y
            if not 0 <= new_a < 5 or not 0 <= new_b < 5:
                continue
            if check[new_a][new_b] == 1:
                continue
            if place[new_a][new_b] == 'O':
                if not search(place, check, new_a, new_b, cnt + 1):
                    return False
            elif place[new_a][new_b] == 'P':
                return False
        return True

    for place in places:
        first(place)

    return answer
