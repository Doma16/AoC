import os
import math
print(os.getcwd())

with open('./day10/example.txt','r') as file:
    inputs = [x.strip() for x in file]

pipes = 'LF7J|-'
orientations = [(1,1), (0,1), (0,0), (1,0), (1,0), (0,1)]

n = len(inputs[0])
grid = [] #[[]] * n

start = None
for row, inp in enumerate(inputs):

    ids = inp.find('S')
    els = list(inp)
    
    if ids != -1:
        start = (row, ids)

    grid.append(els)


def see_round(x, y, grid):
    
    n = len(grid)
    m = len(grid[0])
    
    if x + 1 < n:
        q1 = grid[x+1][y]
    if x - 1 >= 0:
        q3 = grid[x-1][y]
    if y + 1 < m:
        q2 = grid[x][y+1]
    if y - 1 >= 0:
        q4 = grid[x][y-1]

    avail = []
