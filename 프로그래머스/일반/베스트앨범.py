from operator import itemgetter
import sys
sys.stdin = open('베스트앨범.txt')

T = int(input())
for tc in range(T):
    genre = list(map(str, input().split()))
    plays = list(map(int, input().split()))

    genre_playsum = {}
    for i in range(len(genre)):
        if genre[i] not in genre_playsum:
            genre_playsum[genre[i]] = plays[i]
        else:
            genre_playsum[genre[i]] += plays[i]
    genre_playsum = sorted(genre_playsum.items(), key=itemgetter(1), reverse=True)
    print(genre_playsum)

    temp = []
    temp2 = {}
    for i in range(len(plays)):
        temp.append([str(i), plays[i]])
    print(temp)

    for i in range(len(genre)):
        if genre[i] not in temp2:
            temp2[genre[i]] = [temp[i]]
        else:
            temp2[genre[i]] += [temp[i]]
    print(temp2)

    result = []
    for i in genre_playsum:
        print(i[0])
        for key, value in temp2.items():
            if key == i[0]:
                value = sorted(value, key=itemgetter(1), reverse=True)
                if len(value) <= 2:
                    for j in value:
                        result.append(int(j[0]))
                else:
                    for j in range(0, 2):
                        result.append(int(value[j][0]))

    print(result)


