import re
import os
import numpy as np
from tqdm import tqdm
print(os.getcwd())

with open('./day5/example.txt','r') as file:
    input = file.read()

pattern = r'\n\n'
maps = re.split(pattern, input)

part2seeds = []
categories = dict()
for id, map in enumerate(maps):
    name, other = map.split(':')

    lines = other.strip().split('\n')
    
    if id == 0:
        numbers = lines[id].split()
        numbers = [ int(x) for x in numbers ]
        categories[name] = numbers
        repetitions = numbers[1::2]
        starts = numbers[::2]
        for s,r in zip(starts, repetitions):
            part2seeds.append([s,r])
        continue
    else:
        name = name[:-4]

    ranges = []
    for line in lines:
        numbers = line.split()
        numbers = [ int(x) for x in numbers ]
        ranges.append(numbers)        
        
    categories[name] = ranges

locations = []
t_keys = list(categories.keys())[1:]
for seed in categories['seeds']:
    val = seed

    for key in t_keys:
        ranges = categories[key]
        for range_ in ranges:
            if val >= range_[1] and val < range_[1] + range_[2]:
                val = val - (range_[1] - range_[0])
                break

    locations.append(val)

print(f'Part 1: min {min(locations)}')


minL = None
part2seeds = [ [x[0], x[0]+x[1]] for x in part2seeds ]

def range_transform(a,b,n,o,r):
    if b < o:
        return []#[[a,b]]
    if a >= o + r:
        return []#[[a,b]]
    if a >= o:
        if b > o + r:
            return [[a+n-o, n+r-1],[o+r, b]]
        else:
            return [[a+n-o, b+n-o]]
    else:
        if b > o + r:
            return [[n, n+r-1], [a,o-1], [o+r, b]]
        else:
            return [[n, b+n-o], [a, o-1]]

ranges = part2seeds.copy()
t_keys = list(categories.keys())[1:]
new_ranges = []
for id, seed_rng in enumerate(ranges):
    new_rng = [seed_rng.copy()]
    for key in t_keys:
        tmp = []
        while len(new_rng) > 0:
            tformed = False
            for t_ in categories[key]:
                rngs = range_transform(*new_rng[0], *t_)
                if len(rngs) != 0:
                    tformed = True
                    tmp.extend([rngs[0]])
                    new_rng.pop(0)
                    new_rng.extend(rngs[1:])
                if len(new_rng) == 0:
                    break
            if not tformed:
                if len(new_rng) != 0:
                    tmp.extend([new_rng[0].copy()])
                    new_rng.pop(0)
        new_rng = tmp.copy()

    new_ranges.extend(new_rng)
        
minL = new_ranges[0][0]
for rng in new_ranges:
    if min(rng) < minL:
        minL = min(rng)

print(f'Part 2: min {minL}')