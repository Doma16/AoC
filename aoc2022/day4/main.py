import numpy as np
import os 

print(os.getcwd())

with open('../adventOfCode/aoc2022/day4/task.txt','r') as file:
    inputs = [x.strip() for x in file]

sections = inputs
count = 0

for section in sections:
    r1, r2 = section.split(",")
    elf1 = []
    elf2 = []
    numbs1 = r1.split("-")
    numbs2 = r2.split("-")
    for i in range(int(numbs1[0]),int(numbs1[1])+1):
        elf1.append(i)
    for i in range(int(numbs2[0]), int(numbs2[1])+1):
        elf2.append(i)
    
    s = set()
    for e in elf1:
        if e in elf2:
            s.add(e)
    
    if len(s) > 0:
        count += 1
print(count)
