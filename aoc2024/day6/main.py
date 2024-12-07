
file = 'example.txt'

with open(file, 'r') as f:
    data = [x.strip() for x in f.readlines() if x.strip() != '']

orientations = {
    '<': (0, -1),'>': (0, 1),'v': (1, 0),'^': (-1, 0),
}
start, direction = None, None

def rotation(di, dj):
    return dj, -di

#part1

for idy, row in enumerate(data):
    for idx, i in enumerate(row):
        if i in orientations:
            start = (idy, idx)
            direction = orientations[i]

visited = []
directions = []
n, m = len(data), len(data[0])
i, j = start
di, dj = direction
while (0 <= i < n and 0 <= j < m):
    ii = i + di
    jj = j + dj
    visited.append((i, j))
    directions.append((di, dj))
    if not (0 <= ii < n and 0 <= jj < m):
        break

    if data[ii][jj] == '#':
        di, dj = rotation(di, dj)
        continue

    if data[ii][jj] == '.':
        ...

    i, j = ii, jj
    
unique = set(visited)
part1 = len(unique)
print(part1)

#part2
crossing = dict()
over = dict()
for point, direction in zip(visited, directions):
    if point in over:
        crossing[point] =  over[point], direction
    over[point] = direction 


'''
    s
    |
    v
f-->O-->
    |
    v
'''
possible = []
for cross, (first, second) in crossing.items():
    if rotation(*second) == first:
        possible.append(cross)



breakpoint()