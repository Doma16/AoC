import sys

file = sys.argv[1]
with open(file, 'r') as f:
    data = [x.strip() for x in f.readlines() if x.strip() != '']

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = len(data), len(data[0])

pad = '>'
for k in range(len(data)):
    data[k] = pad + data[k] + pad

data.insert(0, pad * (m+2))
data.append(pad * (m+2))

visited = set()
def next(i, j):
    visited.add((i, j))
    el = data[i][j]

    val = 0
    same = 4
    for di, dj in directions:
        ii = i + di
        jj = j + dj
        nel = data[ii][jj]
        
        flag = el == nel
        if flag:
            same -= 1
        
        if (ii, jj) in visited:
            continue
        
        if flag:
            area, bound = next(ii, jj)
            val += area
            same += bound

    #data[i] = data[i][:j] + ' ' + data[i][j+1:]
    return 1 + val, same

comps = []
i = 1
while i <= n:
    j = 1
    while j <= m:
        if (i, j) not in visited:
            area, bound = next(i, j)
            comps.append((data[i][j], area, bound))
        j += 1
    i += 1

print(comps)
#part1
print(sum([a * b for _, a, b in comps]))

# out = ''
# for row in data:
#     out += row + '\n'

# print(out)