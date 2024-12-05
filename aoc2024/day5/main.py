from collections import defaultdict

file = 'input.txt'

with open(file, 'r') as f:
    data = [ x.strip() for x in f.readlines() ][:-1]

idx = data.index('')
rules_data = data[:idx]
updates = data[idx+1:]

rules = defaultdict(list)
for line in rules_data:
    a, b = (int(x) for x in line.split('|'))
    rules[a].append(b)

updates = [[int(y) for y in x.split(',')] for x in updates]

#part1

right_order = []
wrong_order = []
for update in updates:
    left = set()
    right = update.copy()
    n, i = len(right), 0
    good = True
    while i < n and good:
        before = rules.get(right[i], [])
        for el in before:
            if el in left:
                good = False
                break
        left.add(right[i])
        i += 1
    
    if good:
        right_order.append(update)
    else:
        wrong_order.append(update)

part1 = sum([x[len(x)//2] for x in right_order])

#part2
rrules = defaultdict(list)
for r, ll in rules.items():
    for el in ll:
        rrules[el].append(r)    

fixed = []
for update in wrong_order:
    left = []
    right = update.copy()
    for el in right:
        i = 0
        while i < len(left):
            if left[i] in rrules[el]:
                i += 1
                continue
            break
        left.insert(i, el)
    
    fixed.append(left)

part2 = sum([x[len(x)//2] for x in fixed])

print(f'part1: {part1}')
print(f'part2: {part2}')
