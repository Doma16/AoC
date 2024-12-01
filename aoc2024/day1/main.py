from collections import defaultdict

input_f = 'input1.txt'

with open(input_f, 'r') as f:
    data = [ x.strip().split() for x in f.readlines() if x.strip() != '' ]
    
data = [ [int(y) for y in x] for x in data ]

#part1
left = sorted(x[0] for x in data)
right = sorted(x[1] for x in data)

distance = [ abs(x-y) for x,y in zip(left, right)]
total_distance = sum(distance)


#part2
occ = defaultdict(lambda: 0)
for el in right:
    occ[el] += 1

similarity = sum([ x*occ[x] for x in left ])
breakpoint()