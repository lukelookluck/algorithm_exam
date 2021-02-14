from collections import deque
import sys

N = int(sys.stdin.readline().strip())
my_card = deque(list(range(1, N+1)))

while len(my_card) != 1:
    my_card.popleft()
    my_card.append(my_card.popleft())

print(*my_card)