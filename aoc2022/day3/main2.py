import numpy as np

with open('./aoc2022/day3/task.txt','r') as file:
    inputs = [x.strip() for x in file]

compartments = [[inputs[3*i],inputs[3*i+1],inputs[3*i+2]] for i in range(int(len(inputs)/3))]

output = []
i = 0
for input in compartments:
    same = None
    sames = set()
    for i in range(len(input[0])):
        for j in range(len(input[1])):
            if(input[0][i] == input[1][j]):
                    sames.add(input[0][i])
    adding = set()
    for k in range(len(input[2])):
        for s in sames:
            if(input[2][k] == s):
                adding.add(s)
    for a in adding:
        output.append(a)
        
print(output)
def newOrd(c):
    if ord(c) >= 97:
        return ord(c) - 96
    elif ord(c) <= 90:
        return ord(c) - 38

print(np.sum([newOrd(x) for x in output]))