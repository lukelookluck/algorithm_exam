from collections import deque

def check(cards, answer, player, dealer):
    print(player)
    if sum(player) == 21:
        if sum(dealer) == 21:
            answer += 0
        else:
            answer += 3
    if sum(player) < 21:
        while player:
            if 1 in dealer or 7 in dealer:
                if sum(player) < 17:
                    card = cards.popleft()
                    if card > 10:
                        player.append(10)
                    else:
                        player.append(card)
                else:
                    break
            elif 4 in dealer or 5 in dealer or 6 in dealer:
                break
            elif 2 in dealer or 3 in dealer:
                if sum(player) < 12:
                    card = cards.popleft()
                    if card > 10:
                        player.append(10)
                    else:
                        player.append(card)
                else:
                    break
    if sum(player) > 21:
        answer -= 2
    print(player, dealer, cards)



def solution(cards):
    cards = deque(cards)
    answer = 0
    while len(cards):
        player = []
        dealer = []
        for i in range(0, 4):
            if i % 2:
                if cards[0] > 10:
                    dealer.append(10)
                else:
                    dealer.append(cards[0])
            else:
                if cards[0] > 10:
                    player.append(10)
                else:
                    player.append(cards[0])
            cards.popleft()
        print(player, dealer, cards)
        check(cards, answer, player, dealer)
        break



    return answer


cards = [1, 4, 10, 7, 9, 1, 8, 13]
solution(cards)