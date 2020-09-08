import sys
sys.stdin = open('베이비진.txt')

T = int(input())
for tc in range(T):
    data = [*map(int, input().split())]
    print(data)

    player1 = {}
    player2 = {}
    result = 0

    for i in range(len(data)):
        my_bool = False
        if i%2 == 0:
            if data[i] in player1:
                player1[data[i]] += 1
            else:
                player1[data[i]] = 1
        elif i%2 == 1:
            if data[i] in player2:
                player2[data[i]] += 1
            else:
                player2[data[i]] = 1
        # print(i)
        if i >= 4:
            if 3 in player1.values():
                result += 1
                my_bool = True
                break
            else:
                player1_sorted = sorted(player1)
                for i in range(1, len(player1_sorted)-1):
                    if player1_sorted[i-1] + player1_sorted[i+1] == player1_sorted[i] * 2 and player1_sorted[i-1] + 1 == player1_sorted[i]:
                        result += 1
                        my_bool = True
                        break

            if 3 in player2.values():
                result += 2
                my_bool = True
                break
            else:
                player2_sorted = sorted(player2)
                for i in range(1, len(player2_sorted) - 1):
                    if player2_sorted[i-1] + player2_sorted[i+1] == player2_sorted[i] * 2 and player2_sorted[i-1] + 1 == player2_sorted[i]:
                        result += 2
                        my_bool = True
                        break
        if my_bool is True:
            break

    # if result == 0:
    print("#{} {}".format(tc+1, result))


