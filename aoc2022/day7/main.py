import numpy as np

with open('./aoc2022/day7/input.txt','r') as file:
    inputs = [ x.strip() for x in file ]

#print(inputs)

filesystem = [['/']]
prev = None
current = filesystem
root = filesystem[0]

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
                    current.append([file[3:].strip()])
                else:
                    size, name = file.split(" ")
                    size = int(size.strip())
                    name = name.strip()
                    current.append((size,name))
        else:
            # cd
            name = command[2:].strip()
            if name == "..":
                current = prev
            else:
                for e in current:
                    if e.__class__ == list:
                        if e[0] == name:
                            prev = current
                            current = e
    else:
        #not command
        size,name = 1,1
    pos +=1

print(filesystem)