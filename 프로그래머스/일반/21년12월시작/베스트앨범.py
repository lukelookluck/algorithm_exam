from operator import itemgetter


def solution(genres, plays):
    result = []
    genre_total_play = {}
    each_play = {}

    for i in range(len(genres)):
        if genres[i] not in genre_total_play:
            genre_total_play[genres[i]] = plays[i]
        else:
            genre_total_play[genres[i]] += plays[i]
        if genres[i] not in each_play:
            each_play[genres[i]] = [[i, plays[i]]]
        else:
            each_play[genres[i]].append([i, plays[i]])

    print(genre_total_play)

    genre_total_play = sorted(genre_total_play.items(), key=itemgetter(1), reverse=True)

    print(genre_total_play)


    for gp in genre_total_play:
        print(gp)
        cnt = 0
        for x in sorted(each_play[gp[0]], key=lambda x: x[1], reverse=True):
            print(x)
            result.append(x[0])
            cnt += 1
            if cnt >= 2:
                break
    print(result)

    return result


g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
solution(g, p)
