import re
import os
import math
import numpy as np
from collections import Counter
from bisect import insort
print(os.getcwd())

with open('./day7/input.txt','r') as file:
    inputs = [x.strip() for x in file]

strength = 'AKQJT98765432'

hands = [ x.split() for x in inputs]

#five of a kind , set 1 -> 0
#four of a kind, set 2 -> 1
#full house, set 2 -> 2
#three of a kind, set 3 -> 3
#two pair, set 3 -> 4
#one pair, set 4 -> 5
#high card, set 5 -> 6
def strenght_test(hand):
    n = len(strength)
    s_ = [n - strength.find(x) for x in hand]
    return tuple(s_)

def type_test(hand):
    c = Counter(hand)
    n = len(c)
    if n == 1:
        return 6
    elif n == 2:
        if 4 in c.values():
            return 5
        else:
            return 4
    elif n == 3:
        if 3 in c.values():
            return 3
        else:
            return 2
    elif n == 4:
        return 1
    else:
        return 0

cards = []
for hand, bid in hands:
    type = type_test(hand)
    s_ = strenght_test(hand)
    insort(cards, (type, s_, int(bid), hand))

rank = 1
total = 0
for card in cards:
    total += rank*card[2]
    rank += 1

print(f'Part 1: total {total}')

# part 2 messes with part 1
strength = 'AKQT98765432J'
def type_test(hand):
    c = Counter(hand)
    n = len(c)
    if 'J' in c and n > 1:
        n -= 1
        J_ = c['J']
        del c['J']
        tmp = sorted(c.items(), key=lambda x: x[1])
        ky = tmp[-1][0]
        c[ky] += J_
    n = len(c)
    if n == 1:
        return 6
    elif n == 2:
        if 4 in c.values():
            return 5
        else:
            return 4
    elif n == 3:
        if 3 in c.values():
            return 3
        else:
            return 2
    elif n == 4:
        return 1
    else:
        return 0


cards = []
for hand, bid in hands:
    type = type_test(hand)
    s_ = strenght_test(hand)
    insort(cards, (type, s_, int(bid), hand))

rank = 1
total = 0
for card in cards:
    total += rank*card[2]
    rank += 1

print(f'Part 2: total {total}')