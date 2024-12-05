from itertools import product
from collections import defaultdict

file = 'input.txt'

with open(file, 'r') as f:
    data = [x.strip() for x in f.readlines() if x.strip() != '']

#part1
posdir = defaultdict(list)
n, m = len(data), len(data[0])

dirs = []
for p1, p2 in product([-1,0,1], [-1,0,1]):
    if p1 != 0 or p2 != 0:
        dirs.append((p1,p2))

def test_xmas(i, j, dir):
    di, dj = dir
    for a, c in enumerate('XMAS'):
        ii = i + a * di
        jj = j + a * dj
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if data[ii][jj] != c:
            return False
    return True

i = 0
while i < n:
    j = 0
    while j < m:
        for dir in dirs:
            if test_xmas(i, j, dir):
                posdir[(i,j)].append(dir)
        j += 1
    i += 1

part1 = sum([len(x) for x in posdir.values()])


# for i in range(n):
#     for j in range(m):
#         if (i,j) in posdir:
#             cnt = len(posdir[i,j])
#             if cnt > 2:
#                 print(f"\033[42m{cnt}\033[0m",end='')
#             else:
#                 print(f"\033[41m{cnt}\033[0m",end='')
#         else:
#             print(data[i][j],end='')
#     print('__',i)
        
# rows = [0] * n
# for pos, ll in posdir.items():
#     rows[pos[0]] += len(ll)

# print(part1)
# avg = sum(rows)/len(rows)
# print(f'avg: {avg}')
# # for idx, row in enumerate(rows):
# #     print(idx, abs(row-avg) > 10 and row > avg)


#part2
x_mas_dir = defaultdict(list)
check_dirs = [x for x in dirs if abs(x[0]) == 1 and abs(x[1]) == 1] 

def test_mas(i, j, dir):
    di, dj = dir
    for a, c in enumerate('MAS'):
        ii, jj = i + a * di, j + a * dj
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if data[ii][jj] != c:
            return False
    return True

i = 0 
while i < n:
    j = 0
    while j < m:
        for dir in dirs:
            if test_mas(i, j, dir):
                x_mas_dir[(i,j)].append(dir)
        j += 1
    i += 1

part2 = 0
for x, xdirs in x_mas_dir.items():
    i, j = x
    for xdir in xdirs:
        if xdir in check_dirs:
            dis = [0, 2*xdir[0]]
            djs = [2*xdir[1], 0]
            cdirs = [(xdir[0], -xdir[1]), (-xdir[0], xdir[1])]
            for di, dj, cdir in zip(dis, djs, cdirs):
                ii = i + di
                jj = j + dj
                if not (0 <= ii < n and 0 <= jj < m):
                    continue
                odir = x_mas_dir.get((ii, jj), [])
                if cdir in odir:
                    part2 += 1
part2 //= 2

print(part1)
print(part2)