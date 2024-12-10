file = 'input.txt'

with open(file, 'r') as f:
    data = [[ int(y) for y in x.strip()] for x in f.readlines() if x.strip() != '']

trailheads = []
for i, row in enumerate(data):
    for j, el in enumerate(row):
        if el == 0:
            trailheads.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = len(data), len(data[0])

def find_top(start, tops=[]):
    i, j = start
    curr_h = data[i][j]
    if curr_h == 9:
        tops.append((i, j))

    for di, dj in directions:
        if not(0 <= i + di < n and 0 <= j + dj < m):
            continue
        new_h = data[i + di][j + dj]
        if new_h - curr_h == 1:
            find_top((i + di, j + dj), tops=tops)
        

ttrails = 0
total = 0
for th in trailheads:
    tops = []
    find_top(th, tops=tops)
    ttrails += len(tops)
    unique = set(tops)
    total += len(unique)

print(total)
#part2 - already did count it :)
print(ttrails)