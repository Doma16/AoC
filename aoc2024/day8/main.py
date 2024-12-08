from collections import defaultdict

file = 'input.txt'

with open(file, 'r') as f:
    data = [ x.strip() for x in f.readlines() if x.strip() != '' ]


#part1
freq = defaultdict(list)
n, m = len(data), len(data[0])

for i, row in enumerate(data):
    for j, el in enumerate(row):
        if el != '.':
            freq[el].append((i, j))

def generate_antinodes(positions):
    antinodes = []
    nn = len(positions)
    for i, pos in enumerate(positions):
        pi, pj = pos
        j = i + 1
        while j < nn:
            ppi, ppj = positions[j]

            di = pi - ppi
            dj = pj - ppj

            antinodes.append((pi + di, pj + dj))
            antinodes.append((ppi - di, ppj - dj))

            j += 1

    return antinodes

total = []
for f, positions in freq.items():
    total.extend(generate_antinodes(positions))

i = 0
while i < len(total):
    pi, pj = total[i]
    if not (0 <= pi < n and 0 <= pj < m):
        total.pop(i)
    else:
        i += 1
 
total = set(total)
part1 = len(total)
print(part1)

def generate_antinodes_harmonics(positions):
    antinodes = []
    nn = len(positions)
    for i, pos in enumerate(positions):
        pi, pj = pos
        j = i + 1
        while j < nn:
            ppi, ppj = positions[j]

            ki = pi - ppi
            kj = pj - ppj

            di, dj = 0, 0
            while (0 <= pi + di < n and 0 <= pj + dj < m):
                antinodes.append((pi + di, pj + dj))
                di += ki
                dj += kj

            di, dj = 0, 0
            while (0 <= ppi + di < n and 0 <= ppj + dj < m):
                antinodes.append((ppi + di, ppj + dj))
                di -= ki
                dj -= kj

            j += 1

    return antinodes

part2 = []
for f, positions in freq.items():
    part2.extend(generate_antinodes_harmonics(positions))

i = 0
while i < len(part2):
    pi, pj = part2[i]
    if not (0 <= pi < n and 0 <= pj < m):
        part2.pop(i)
    else:
        i += 1

part2 = len(set(part2))
print(part2)