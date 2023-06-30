import numpy as np
import os 
import time

print(os.getcwd())

with open('input2.txt', 'r') as file:
    inputs = [x.strip().split(' ') for x in file]


start = time.perf_counter()
# R L U D
move_dict = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
inputs = [ (move_dict[x[0]], int(x[1])) for x in inputs ]

s = (0,0)
H = s
T = s

visited = set()
visited.add(s)

def coord_add(c1, c2):
    return (c1[0]+c2[0], c1[1]+c2[1])

def calc_move_tail(H,T):
    dx = H[0] - T[0]
    dy = H[1] - T[1]
    
    # diagonal move
    if H[0] != T[0] and H[1] != T[1] and abs(dx)+abs(dy) > 2:
        mv_x = -1
        mv_y = -1
        if dx > 0: mv_x = 1
        if dy > 0: mv_y = 1
        return coord_add(T, (mv_x,mv_y))

    # x move
    if abs(dx) > 1:
        mv_x = -1
        if dx > 0: mv_x = 1
        return coord_add(T, (mv_x, 0))

    # y move
    if abs(dy) > 1:
        mv_y = -1
        if dy > 0: mv_y = 1
        return coord_add(T, (0, mv_y))

    return T

'''
for input in inputs:
    for i in range(input[1]):
        H = coord_add(H, input[0])
        T = calc_move_tail(H, T)
        visited.add(T)

print(len(visited))
'''
print(f'{time.perf_counter() - start:.4f}s')



#part 2 - more knots
s = (0,0)
visited = set()
visited.add(s)
H = s
knots = [s for _ in range(9)]

for input in inputs:
    for i in range(input[1]):
        H = coord_add(H, input[0])
        prev = H
        for j in range(len(knots)):
            knots[j] = calc_move_tail(prev, knots[j])
            prev = knots[j]
        visited.add(knots[8])

print(len(visited))
print(f'{time.perf_counter() - start:.4f}s')