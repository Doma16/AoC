import numpy as np

with open('./aoc2022/day3/input.txt','r') as file:
    inputs = [x.strip() for x in file]

compartments = [[x[:int(x.__len__()/2)], x[int(x.__len__()/2):]] for x in inputs ]
sames = []

for input in compartments:
    i = 0
    same = None
    for i in range(input[0].__len__()):
        for j in range(input[1].__len__()):
            if input[0][i] == input[1][j]:
                same = input[0][i]

    sames.append(same)

def newOrd(c):
    if ord(c) >= 97:
        return ord(c) - 96
    elif ord(c) <= 90:
        return ord(c) - 38

print(np.sum([newOrd(c) for c in sames]))
