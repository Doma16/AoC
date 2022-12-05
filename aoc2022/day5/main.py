import numpy as np
import os 

print(os.getcwd())

with open('../adventOfCode/aoc2022/day5/task.txt','r') as file:
    inputs = [x for x in file]

stack = list()
command = list()

part = 0
for input in inputs:
    if input == "\n":
        part+=1
    elif part == 0:
        stack.append(input)
    elif part == 1:
        command.append(input.strip())

print(stack[1].split(" "))
Nstacks = int(stack[-1].split(" ")[-2])
Nelements = len(stack) - 1
print(Nstacks)
print(Nelements)

stacks = [list() for _ in range(Nstacks)]
for i in range(Nelements-1,-1,-1):
    elems = []
    for g in range(0,3*Nstacks + Nstacks - 1,4): 
        elems.append(stack[i][g:g+3])
    for j in range(Nstacks):
        if(elems[j].strip() != ''):
            stacks[j].append(elems[j].strip())

print(stacks)

for c in command:
    n1,Nmove,n3,Nfrom,n5,Nto = c.split(" ")
    Nmove = int(Nmove)
    Nfrom = int(Nfrom)-1
    Nto = int(Nto)-1
    temp = []
    for i in range(Nmove):
        temp.append(stacks[Nfrom].pop())
    
    for i in range(Nmove):
        stacks[Nto].append(temp.pop())

word = ""
for s in stacks:
    word += s.pop()[1]
print(word)