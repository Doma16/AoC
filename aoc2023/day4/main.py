import re
import os
import numpy as np
print(os.getcwd())

with open('./day4/input.txt','r') as file:
    inputs = [x.strip() for x in file]

count_matches = []
cards = dict()
for card in inputs:
    card = card[4:]
    card_id, rest = card.split(':')
    card_id = int(card_id)
    cards[card_id] = 1 + cards.setdefault(card_id, 0)

    winning, my = rest.split('|')
    winning = set(winning.strip().split())
    my = set(my.strip().split())
    
    matches = [x for x in my if x in winning]
    count_matches.append(matches)

    for id in range(card_id+1, card_id+len(matches)+1, 1):
        cards.setdefault(id, 0)
        cards[id] += cards[card_id]



count = [len(x) for x in count_matches]
pow2 = [2**(x-1) for x in count if x > 0]

print(f'Part 1: sum {sum(pow2)}')
print(f'Part 2: sum {sum(cards.values())}')