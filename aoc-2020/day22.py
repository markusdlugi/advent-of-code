from collections import deque
from itertools import islice
from timeit import default_timer as timer

start = timer()
with open("input/22.txt") as field:
    players = [section.splitlines() for section in field.read().split("\n\n")]

player1 = deque([int(x) for x in players[0][1:]])
player2 = deque([int(x) for x in players[1][1:]])


def combat(player1, player2, recursive):
    seen_rounds = set()
    while player1 and player2:
        round_ = (tuple(player1), tuple(player2))
        if recursive and round_ in seen_rounds:
            # Round seen already, P1 wins
            player1.clear()
            player2.clear()
            player1.append(0)
        else:
            seen_rounds.add(round_)

            c1 = player1.popleft()
            c2 = player2.popleft()

            if recursive and c1 <= len(player1) and c2 <= len(player2):
                p1_wins, _ = combat(deque(islice(player1, 0, c1)), deque(islice(player2, 0, c2)), recursive)
            else:
                p1_wins = c1 > c2

            if p1_wins:
                player1.append(c1)
                player1.append(c2)
            else:
                player2.append(c2)
                player2.append(c1)

    p1_won = len(player1) > 0
    return p1_won, player1 if p1_won else player2


def score(deck):
    return sum(deck[-i] * i for i in range(1, len(deck) + 1))


_, winning_deck = combat(player1.copy(), player2.copy(), False)
print(score(winning_deck))
_, winning_deck = combat(player1, player2, True)
print(score(winning_deck))

end = timer()
print(f'Took {round((end - start) * 1000, 2)} ms.')