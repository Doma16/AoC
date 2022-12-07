import numpy as np

with open('./aoc2022/day7/task.txt','r') as file:
    inputs = [ x.strip() for x in file ]

#print(inputs)
            # 0    # 1    #  2    #  3
            #name, #dirs, #files, #previous
filesystem = ['/', list(), list(), None]
current = filesystem
dirs = []

pos = 0
n = len(inputs)
while(pos < n):
    if inputs[pos][0] == '$':
        #command
        command = inputs[pos][2:]
        if command == 'ls':
            while(pos+1 < n and inputs[pos+1][0] != '$'):
                pos+=1
                file = inputs[pos]
                if file[:3] == 'dir':
                    newDir = [file[3:].strip(), list(), list(), current]
                    current[1].append(newDir)
                    dirs.append(newDir)
                else:
                    size, name = file.split(" ")
                    size = int(size.strip())
                    name = name.strip()
                    current[2].append((size,name))
        else:
            # cd
            name = command[2:].strip()
            if name == "..":
                current = current[3]
            elif name == "/":
                current = filesystem
            else:
                for e in current[1]:
                    if e[0] == name:
                        current = e
    else:
        #not command
        size,name = 1,1
    pos +=1

#print(filesystem)
#done filesystem - weird implementation

def sumDIR(l):
    sum = 0
    for f in l[2]:
        sum += f[0]
    for dirs in l[1]:
        sum += sumDIR(dirs)
    return sum

#print(sumDIR(filesystem))
#working sum dir function
#now need to iterate over dirs

max_size = 1e5
size = 0
for dir in dirs:
    val = sumDIR(dir)
    if val < max_size:
        size += val


print(size)

#part 2

disk_space = 70000000
unused = 30000000
current_allocation = sumDIR(filesystem)

diff = disk_space - current_allocation

minimal = current_allocation
for dir in dirs:
    deldiff = sumDIR(dir)
    if current_allocation - deldiff < disk_space - unused:
        if deldiff < minimal:
            minimal = deldiff

print(minimal)   